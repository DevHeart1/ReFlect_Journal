# ReFlect Journaling App - Core User Flows

**Version:** 1.1
**Date:** May 1, 2025

## 1. Introduction

This document illustrates the primary user interaction flows for the ReFlect Journaling Web Application MVP. These flows describe the step-by-step journey users take to accomplish key tasks within the application, based on the requirements defined in the PRD.

## 2. Personas (Illustrative)

*   **Alex (The Mindful Explorer):** Uses ReFlect daily to process thoughts and track emotional patterns. Values insights and a calming interface.
*   **Sam (The Busy Professional):** Uses ReFlect periodically to de-stress and capture significant moments. Values efficiency and reminders.

## 3. Core User Flows (MVP)

### 3.1 Onboarding & Authentication Flow

*   **Goal:** New user securely registers, or existing user securely logs in.
*   **Trigger:** User navigates to the application's root URL.

1.  **Landing/Login Page:** Presents a clean interface with options: "Log In" and "Sign Up". May include brief value proposition text.
2.  **Sign Up Path:**
    *   User selects "Sign Up".
    *   Displays registration form: Email, Password (with strength indicator), Confirm Password. Includes link to Terms of Service/Privacy Policy.
    *   User fills form and submits.
    *   **Client-side validation:** Basic checks (e.g., format, matching passwords).
    *   **Backend Interaction (Supabase Auth):** Securely registers the user via Supabase client library.
    *   **On Success:** User session is created (Supabase handles JWT). Redirects to the main application view (e.g., Journal Timeline).
    *   **On Failure:** Displays clear error message (e.g., "Email already exists", "Password too weak").
3.  **Log In Path:**
    *   User selects "Log In".
    *   Displays login form: Email, Password. Includes "Forgot Password?" link.
    *   User fills form and submits.
    *   **Backend Interaction (Supabase Auth):** Securely authenticates the user via Supabase client library.
    *   **On Success:** User session is established. Redirects to the main application view.
    *   **On Failure:** Displays clear error message (e.g., "Invalid credentials").
4.  **Forgot Password Path:**
    *   User clicks "Forgot Password?".
    *   Displays form requesting registered email.
    *   User submits email.
    *   **Backend Interaction (Supabase Auth):** Initiates password reset flow (Supabase sends reset email).
    *   User receives email, clicks link, sets new password via a secure page.

### 3.2 Creating & Editing a Journal Entry

*   **Goal:** User creates a new entry or modifies an existing one with text, optional photo, mood, and tags.
*   **Trigger:** User clicks "New Entry" button (or similar) or "Edit" on an existing entry.

1.  **Navigate to Editor:** Application displays the Journal Entry Editor view.
    *   If new: Blank editor with current date pre-filled (editable).
    *   If editing: Populates editor with existing entry content, date, media, mood, tags.
2.  **Compose/Edit Text:** User interacts with the Rich Text Editor, applying formatting as needed.
    *   **Autosave (Draft):** Implement periodic background saving to prevent data loss (local storage or lightweight backend call).
3.  **Add/Change Date:** User can modify the entry date using a date picker.
4.  **Add/Manage Photo(s):**
    *   User clicks "Add Photo" icon/button.
    *   System file picker appears. User selects one or more photos (respecting limits).
    *   **Frontend:** Displays thumbnail previews, shows upload progress.
    *   **Backend Interaction:** Photos are securely uploaded (directly to Supabase Storage via client or proxied through Django backend) upon saving the entry. Association stored in DB.
    *   User can remove attached photos before saving.
5.  **Log Mood:**
    *   User interacts with the mood selection element (e.g., clicks an emoji scale).
    *   Selected mood is visually indicated.
6.  **Add/Manage Tags:**
    *   User types in the tag input field.
    *   System suggests existing tags based on input.
    *   User can select suggestions or type a new tag and press Enter/Comma.
    *   Added tags are displayed visually (e.g., as pills), removable by clicking 'x'.
7.  **Save Entry:**
    *   User clicks "Save" or "Done".
    *   **Frontend Validation:** Ensures required fields (if any) are filled.
    *   **Backend Interaction (Django API):** Sends entry data (text, date, mood, tags, media references) to the backend API (POST for new, PUT/PATCH for edit).
    *   **Backend Logic:** Validates data, saves text/metadata to PostgreSQL, ensures media references are linked, triggers asynchronous AI sentiment analysis.
    *   **On Success:** Displays confirmation (e.g., toast notification "Entry Saved"). Redirects user to the Journal Timeline/List view, showing the new/updated entry.
    *   **On Failure:** Displays clear error message.

### 3.3 Viewing Journal Entries & Insights

*   **Goal:** User browses their journal history and views associated data, including AI sentiment.
*   **Trigger:** User is logged in and navigates the main application areas.

1.  **Journal Timeline/List View (Default):**
    *   Displays entries chronologically (newest first) in a summarized format (e.g., date, title/snippet, mood emoji, tags, photo thumbnail if present).
    *   Implements pagination or infinite scrolling for large numbers of entries.
    *   **Backend Interaction:** Fetches paginated entry list from Django API.
2.  **Filtering by Tag:**
    *   User clicks on a tag displayed in the timeline or selects from a dedicated filter area.
    *   Timeline updates to show only entries containing the selected tag(s).
    *   **Backend Interaction:** Fetches filtered entry list from Django API.
3.  **Searching Entries:**
    *   User types keywords into a search bar.
    *   Search results page/view displays matching entries.
    *   **Backend Interaction:** Sends search query to Django API (leveraging DB search capabilities).
4.  **Viewing Entry Detail:**
    *   User clicks on a specific entry summary in the timeline/list/search results.
    *   Navigates to the Entry Detail view.
    *   Displays full entry content (rich text rendered), date, mood, tags, full-size photos.
    *   Displays the AI-generated sentiment analysis result (e.g., "Sentiment: Positive (0.85)").
    *   Provides "Edit" and "Delete" options.
    *   **Backend Interaction:** Fetches detailed data for the specific entry ID from Django API.

### 3.4 Managing Settings

*   **Goal:** User configures application preferences like theme, reminders, and data export.
*   **Trigger:** User navigates to the "Settings" area.

1.  **Navigate to Settings:** User accesses the dedicated Settings page.
2.  **Theme Selection:**
    *   User selects "Light" or "Dark" theme option (e.g., toggle switch, radio buttons).
    *   UI immediately updates to reflect the chosen theme. Preference is saved locally (e.g., localStorage) and potentially synced to user profile on backend.
3.  **Reminder Configuration:**
    *   User enables/disables reminders.
    *   If enabled, user selects desired time and frequency (e.g., Daily at 9:00 PM).
    *   User saves reminder settings.
    *   **Backend Interaction:** Sends reminder preferences to Django API. Backend schedules/updates notification tasks.
4.  **Data Export:**
    *   User clicks "Export My Data".
    *   **Backend Interaction:** Initiates data export process via Django API.
    *   **Backend Logic:** Generates JSON file containing user's entries and metadata.
    *   **Frontend:** Provides download link/initiates file download once ready. Displays progress/confirmation.

## 4. Notes

*   These flows prioritize clarity and core functionality for the MVP.
*   Robust error handling and clear user feedback (loading states, success/error messages) are crucial at every step involving backend interaction.
*   UI/UX details (specific icons, layout, animations) will be defined in design mockups but should align with the professional and calming aesthetic goal.
*   Asynchronous operations (AI analysis, potentially autosave) must provide appropriate UI feedback without blocking the user.
