# ReFlect Journaling App - Product Requirements Document (PRD)

**Version:** 1.1
**Date:** May 1, 2025
**Status:** Draft

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the ReFlect Journaling Application (Phase 1 - Web MVP). ReFlect is envisioned as a premium, AI-enhanced digital sanctuary for self-reflection, emotional awareness, and personal growth. It aims to provide users with an intuitive, beautiful, and secure platform to capture their thoughts, feelings, and experiences, augmented by intelligent insights derived from their entries.

### 1.2 Scope (MVP)
The initial release (MVP) will focus on delivering a core set of features via a responsive web application. Key areas include secure user authentication, rich-text journaling, basic multimedia (photo) uploads, mood tracking, tagging, timeline view, foundational AI-driven sentiment analysis (via Gemini API), user settings (reminders, export), and a highly polished user interface. Features like video/voice journaling, advanced AI insights, goal setting, sharing, and community aspects are planned for subsequent phases.

### 1.3 Goals & Objectives
*   **User Engagement:** Foster consistent journaling habits through an inviting interface, relevant prompts, and gentle reminders.
*   **Self-Awareness:** Empower users with AI-driven insights (starting with sentiment) into their emotional landscape.
*   **Usability:** Deliver a seamless, intuitive, and aesthetically pleasing user experience across desktop and mobile web browsers.
*   **Security & Privacy:** Guarantee the confidentiality and integrity of user data as a paramount priority.
*   **Technical Foundation:** Establish a scalable and maintainable architecture (Next.js, Django, Supabase) to support future growth.

## 2. Target Audience

*   **Primary:** Individuals actively seeking tools for mental wellness, mindfulness, self-discovery, and emotional regulation (Age 18-55, tech-savvy).
*   **Secondary:** Users interested in quantified self, life logging, or therapy support tools.
*   **Characteristics:** Value privacy, appreciate good design, motivated by personal growth, comfortable with digital tools.

## 3. Functional Requirements (FR)

*(Requirements are tagged FR-XXX and prioritized for MVP unless otherwise noted)*

### 3.1 User Authentication & Profile (Powered by Supabase Auth)
*   **FR-001 (P1):** Users must be able to register securely using email and password.
*   **FR-002 (P1):** Users must be able to log in securely using their registered credentials.
*   **FR-003 (P1):** Implement a secure "Forgot Password" / password reset flow.
*   **FR-004 (P1):** Users must be able to log out.
*   **FR-005 (P1):** Users must be able to view and update basic profile information (e.g., name, email - managed via Supabase where applicable).
*   **FR-006 (P2):** Users should be able to delete their account and associated data.
*   **FR-007 (P2):** Explore social login options (Google, Apple).

### 3.2 Journal Entry Management
*   **FR-010 (P1):** Users must be able to create a new journal entry with a specific date (defaults to current).
*   **FR-011 (P1):** The entry editor must support rich text formatting (bold, italics, underline, bullet points, numbered lists, headers).
*   **FR-012 (P1):** Entries must be automatically saved periodically (draft state) and explicitly saved by the user.
*   **FR-013 (P1):** Users must be able to view a list/timeline of their past journal entries, sorted chronologically (newest first).
*   **FR-014 (P1):** Users must be able to view the full content of a selected journal entry.
*   **FR-015 (P1):** Users must be able to edit existing journal entries.
*   **FR-016 (P1):** Users must be able to delete journal entries (with confirmation).
*   **FR-017 (P1):** Each entry must store creation and last modified timestamps.

### 3.3 Multimedia Integration
*   **FR-020 (P1):** Users must be able to upload and attach one or more photos to a journal entry.
*   **FR-021 (P1):** Uploaded photos must be displayed within the entry view.
*   **FR-022 (P1):** Implement constraints on file size and acceptable formats for photos.
*   **FR-023 (P2):** Users should be able to upload and attach videos.
*   **FR-024 (P2):** Users should be able to record/upload voice notes.
*   **FR-025 (P2):** Implement voice-to-text transcription for voice notes.

### 3.4 Organization & Retrieval
*   **FR-030 (P1):** Users must be able to add freeform tags to journal entries during creation or editing.
*   **FR-031 (P1):** The system should suggest previously used tags.
*   **FR-032 (P1):** Users must be able to filter the journal timeline/list by selecting one or more tags.
*   **FR-033 (P1):** Users must be able to search entries by keywords within the entry content and tags.
*   **FR-034 (P2):** Implement a dedicated Calendar view showing days with entries.
*   **FR-035 (P2):** Allow users to define and assign categories (more structured than tags).

### 3.5 AI-Powered Insights (via Gemini API)
*   **FR-040 (P1):** The system must asynchronously perform sentiment analysis (e.g., positive, negative, neutral, score) on saved journal entries using the Gemini API.
*   **FR-041 (P1):** The calculated sentiment must be stored and associated with the entry.
*   **FR-042 (P1):** Users must be able to view the sentiment analysis result for individual entries.
*   **FR-043 (P2):** Display sentiment trends over time (e.g., weekly/monthly chart) in an "Insights" section.
*   **FR-044 (P2):** Identify and display recurring emotional patterns or key themes based on aggregated entry analysis.
*   **FR-045 (P2):** Generate context-aware "Smart Prompts" based on recent entries or identified patterns.
*   **FR-046 (P2):** Explore correlation analysis between logged moods and activities/entry themes.

### 3.6 Mood Tracking
*   **FR-050 (P1):** Users must be able to optionally log their overall mood for a day or associate it directly with an entry (e.g., using a predefined scale, emojis).
*   **FR-051 (P1):** Logged moods should be visually represented alongside entries in the timeline/list view.
*   **FR-052 (P2):** Provide visualizations of mood history/trends over time.

### 3.7 Customization & Settings
*   **FR-060 (P1):** Users must be able to switch between at least two application themes (e.g., Light, Dark).
*   **FR-061 (P1):** Users must be able to configure journaling reminders (time of day, frequency).
*   **FR-062 (P1):** Users must be able to initiate an export of their journal data (e.g., JSON format).
*   **FR-063 (P2):** Allow customization of font size and potentially font family.
*   **FR-064 (P2):** Provide predefined entry templates (e.g., Gratitude, Daily Stoic).
*   **FR-065 (P3):** Allow users to create and save custom templates.

### 3.8 Engagement & Motivation
*   **FR-070 (P1):** Implement backend logic for reminder notifications (delivery mechanism TBD - email, browser push).
*   **FR-071 (P2):** Provide optional daily writing prompts (static list initially, AI-driven later).
*   **FR-072 (P2):** Implement tracking and recognition of journaling streaks/milestones.

### 3.9 Sharing & Community (Deferred - P3+)
*   **FR-080 (P3):** Allow users to share specific, anonymized entries via a unique link.
*   **FR-081 (P3):** Explore opt-in, moderated community features.

### 3.10 Goal Setting (Deferred - P2/P3)
*   **FR-090 (P2):** Allow users to define personal goals.
*   **FR-091 (P3):** Allow users to track progress and link entries to goals.

### 3.11 Premium Features (Deferred - P2/P3)
*   **FR-100 (P2):** Implement subscription management and payment integration (e.g., Stripe).
*   **FR-101 (P2):** Define and gate specific premium features (e.g., advanced AI insights, unlimited video storage, advanced export formats, exclusive themes/templates).

### 3.12 Support
*   **FR-110 (P1):** Provide access to basic FAQs or help documentation.
*   **FR-111 (P2):** Implement a contact form or channel for user support requests.

## 4. Non-Functional Requirements (NFR)

*   **NFR-001 (Performance):** Web application load times (LCP) should be < 2.5 seconds. API response times for typical requests should be < 500ms (excluding external AI calls).
*   **NFR-002 (Scalability):** Backend architecture must support scaling to handle at least 10,000 concurrent users (target for future growth). Database and storage should scale seamlessly (leveraging Supabase capabilities).
*   **NFR-003 (Availability):** Target 99.9% uptime for core services (excluding planned maintenance). Leverage platform features (Supabase, Render, Vercel) for high availability.
*   **NFR-004 (Security):** Adhere to OWASP Top 10. All sensitive data encrypted at rest and in transit. Implement robust authentication/authorization via Supabase. Pass external security audit post-MVP.
*   **NFR-005 (Usability):** Interface must be highly intuitive, requiring minimal user training. Consistent design language and predictable interactions. WCAG 2.1 AA accessibility compliance.
*   **NFR-006 (Maintainability):** Codebase must adhere strictly to documented guidelines (`frontend_guidelines.md`, `backend_guidelines.md`). High test coverage (>80% for backend logic). Modular design.
*   **NFR-007 (Reliability):** Implement comprehensive error handling and logging. Ensure data integrity through database constraints and transactional logic where appropriate. Leverage Supabase automated backups.
*   **NFR-008 (Compatibility):** Web application must function correctly on the latest two versions of major browsers (Chrome, Firefox, Safari, Edge) on desktop and mobile.
*   **NFR-009 (Data Privacy):** Comply with GDPR / CCPA regulations. Provide clear user control over data and export capabilities.

## 5. Design & UX Considerations

*   **Aesthetics:** Aim for a clean, minimalist, calming, and modern visual design. Focus on typography, whitespace, and subtle animations.
*   **User Flow:** Optimize common tasks like creating and viewing entries for speed and efficiency.
*   **Responsiveness:** Ensure a seamless experience across various screen sizes, from mobile browsers to large desktops.
*   **Feedback:** Provide clear visual feedback for user actions, loading states, and errors.
*   **Onboarding:** Consider a brief, welcoming onboarding experience for new users (post-MVP).

## 6. Future Considerations / Out of Scope (MVP)

*   Native Mobile Applications (iOS/Android)
*   Advanced Calendar Integration (External Calendars)
*   Voice Journaling & Transcription
*   Video Uploads & Storage
*   Advanced AI Insights (Pattern detection, Correlation, Smart Prompts)
*   Goal Setting & Tracking
*   Sharing Features (Public/Anonymous)
*   Community Features
*   Advanced Customization (Custom Templates)
*   Data Import Functionality
*   Offline Support (potentially via PWA features later)
*   Full Subscription/Billing Integration

## 7. Open Questions

*   Specific metrics/visualizations for sentiment trends (P2)?
*   Detailed requirements for reminder delivery mechanism (Email? Push?)?
*   Specific data export formats required beyond JSON?
*   Detailed requirements for potential future sharing mechanisms?
