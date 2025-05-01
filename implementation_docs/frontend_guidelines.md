# ReFlect Journaling App - Frontend Development Guidelines

**Version:** 1.1
**Date:** May 1, 2025

## 1. Introduction

This document establishes the standards, conventions, and best practices for frontend development on the ReFlect Journaling Web Application. Built with Next.js and TypeScript, the goal is to create a highly performant, maintainable, accessible, and visually stunning user experience. Adherence to these guidelines is crucial for team collaboration and long-term project health.

## 2. Core Technologies & Libraries

*(Refer to `tech_stack.md` for the definitive specification)*

*   **Framework:** Next.js (v14+ App Router)
*   **Language:** TypeScript (Strict Mode)
*   **UI Styling:** Tailwind CSS
*   **UI Components:** Shadcn/UI (or potentially Material UI - TBD)
*   **State Management:** Zustand (preferred), React Context (simple cases)
*   **Data Fetching/Caching:** React Query (TanStack Query)
*   **Forms:** React Hook Form
*   **Rich Text Editor:** TipTap
*   **Routing:** Next.js App Router
*   **Linting:** ESLint (with Next.js, TypeScript, Tailwind plugins)
*   **Formatting:** Prettier
*   **Testing:** Jest, React Testing Library, Playwright (for E2E)

## 3. Code Style & Formatting

*   **Automation:** ESLint and Prettier are mandatory and configured to run via pre-commit hooks (Husky + lint-staged). All code must pass linting and formatting checks before merging.
*   **Configuration:** Utilize shared ESLint/Prettier configurations committed to the repository (`.eslintrc.json`, `prettier.config.js`, `tailwind.config.js`, `tsconfig.json`).
*   **Naming Conventions:**
    *   Components (File & Function): `PascalCase.tsx` (e.g., `JournalEditor.tsx`)
    *   Variables/Functions: `camelCase`
    *   Constants: `UPPER_SNAKE_CASE`
    *   Types/Interfaces: `PascalCase` (Prefix with `I` or suffix with `Type` if preferred, maintain consistency).
    *   CSS Utility Classes (Tailwind): Follow Tailwind conventions.
*   **TypeScript:**
    *   Enable `strict` mode in `tsconfig.json`.
    *   Use explicit types (`any` is strongly discouraged). Define interfaces/types for props, API responses, and complex objects.
    *   Leverage utility types (e.g., `Partial`, `Omit`, `Pick`) where appropriate.

## 4. Project Structure (Next.js App Router)

Adhere to the Next.js App Router conventions. A feature-based or hybrid structure within `app` is recommended.

```
app/
├── layout.tsx                # Root layout (html, body tags)
├── default.tsx               # Root parallel route default (optional)
├── loading.tsx               # Root loading UI
├── error.tsx                 # Root error UI
├── global.css                # Global styles (Tailwind base/components/utilities)
├── api/                      # API Routes (BFF - Backend for Frontend)
│   └── ...
├── (marketing)/              # Route group for marketing pages (e.g., landing)
│   ├── page.tsx
│   └── layout.tsx
├── (app)/                    # Route group for authenticated app experience
│   ├── layout.tsx            # Main app layout (sidebar, header)
│   ├── default.tsx           # Default view for parallel routes within (app)
│   ├── dashboard/
│   │   └── page.tsx
│   ├── journal/
│   │   ├── page.tsx          # Journal timeline/list
│   │   ├── [entryId]/
│   │   │   ├── page.tsx      # View specific entry
│   │   │   └── loading.tsx   # Loading UI for entry detail
│   │   └── new/
│   │       └── page.tsx      # Create new entry page
│   ├── settings/
│   │   └── page.tsx
│   └── insights/
│       └── page.tsx
├── components/               # Reusable components
│   ├── ui/                   # Generic UI elements (from Shadcn/UI - Button, Input, etc.)
│   ├── forms/                # Form-specific components (e.g., FieldWrapper)
│   └── features/             # Components tied to specific features
│       ├── journal/          # e.g., JournalCard, JournalEditor
│       └── auth/             # e.g., LoginForm
├── lib/                      # Utility functions, constants, helper classes
│   ├── utils.ts
│   ├── constants.ts
│   └── validators.ts         # Zod schemas for validation
├── hooks/                    # Custom React hooks (e.g., useAuth, useMediaQuery)
├── services/                 # API interaction layer (functions calling Django backend)
│   ├── api-client.ts         # Axios or fetch instance setup
│   └── journalService.ts
├── store/                    # Global state (Zustand stores)
│   └── useAuthStore.ts
└── types/                    # Global TypeScript definitions (api-types.ts, etc.)
public/                       # Static assets (images, fonts)
middleware.ts                 # Next.js middleware (e.g., for auth redirects)
next.config.mjs               # Next.js configuration
tailwind.config.ts            # Tailwind configuration
postcss.config.js             # PostCSS configuration
tsconfig.json                 # TypeScript configuration
```

## 5. Component Design

*   **Server vs. Client Components:** Understand and leverage the distinction in the App Router. Default to Server Components unless client-side interactivity (`useState`, `useEffect`, event handlers) is required. Fetch data primarily in Server Components where possible.
*   **Composition:** Build complex UI by composing smaller, single-purpose components.
*   **Props:** Define clear, typed props using TypeScript interfaces/types. Avoid overly complex prop drilling (use Context or state management).
*   **Readability:** Keep components concise and focused. Extract complex logic into custom hooks or utility functions.
*   **Reusability:** Identify and build generic UI elements (`components/ui/`) and feature-specific reusable components (`components/features/`).

## 6. State Management (Zustand)

*   **Stores:** Create separate stores for distinct domains of global state (e.g., `useAuthStore`, `useSettingsStore`).
*   **Selectors:** Use selectors within components to subscribe only to the necessary state slices, preventing unnecessary re-renders.
*   **Immutability:** Treat state as immutable. Use spread syntax or immutable update libraries if needed (Zustand often handles this internally).
*   **Persistence:** Use Zustand middleware (`persist`) for persisting state to `localStorage` (e.g., theme preference) when appropriate.
*   **Local State:** Use `useState` for component-specific, non-shared state.

## 7. Data Fetching & Caching (React Query)

*   **Hooks:** Use React Query hooks (`useQuery`, `useMutation`) for all interactions with the Django backend API.
*   **Query Keys:** Define clear and consistent query keys, often including identifiers, to manage caching effectively.
*   **Stale-While-Revalidate:** Leverage React Query's default caching strategy for a good balance of freshness and performance. Configure `staleTime` and `cacheTime` appropriately based on data volatility.
*   **Mutations:** Use `useMutation` for creating, updating, or deleting data. Implement query invalidation or optimistic updates for a smoother UX.
*   **API Service Layer:** Keep actual `fetch`/`axios` calls within the `services/` directory, called by React Query query/mutation functions.

## 8. Styling (Tailwind CSS + Shadcn/UI)

*   **Utility-First:** Embrace Tailwind's utility-first approach for styling.
*   **Component Abstraction:** Encapsulate common Tailwind patterns within reusable React components (especially using `@apply` sparingly or within component definitions).
*   **Shadcn/UI:** Leverage Shadcn/UI components as a base, customizing them via props and Tailwind classes as needed. Copy components into the project (`components/ui/`) for full control.
*   **Theming:** Configure `tailwind.config.js` for theme customization (colors, fonts, spacing) to match design specifications. Utilize CSS variables for dynamic theming (e.g., light/dark mode).
*   **Responsiveness:** Use Tailwind's responsive modifiers (e.g., `md:`, `lg:`) extensively.

## 9. Routing & Layouts (Next.js App Router)

*   **File-based Routing:** Understand how folder/file structure defines routes.
*   **Layouts:** Utilize `layout.tsx` files for shared UI structures within route segments.
*   **Loading UI:** Implement `loading.tsx` for automatic loading states during navigation using React Suspense.
*   **Error Handling:** Implement `error.tsx` for handling errors within route segments.
*   **Route Groups:** Use route groups `(folderName)` to organize routes without affecting the URL path (e.g., for different layouts like `(app)` vs `(marketing)`).
*   **Linking:** Use the `next/link` component for client-side navigation.
*   **Programmatic Navigation:** Use the `useRouter` hook (from `next/navigation`) for programmatic redirects.
*   **Middleware:** Use `middleware.ts` for tasks like authentication checks and redirects before rendering a page.

## 10. Forms (React Hook Form)

*   **Controlled/Uncontrolled:** Use React Hook Form for efficient form state management.
*   **Validation:** Integrate with validation libraries like **Zod** (`@hookform/resolvers/zod`) for schema-based validation.
*   **Error Handling:** Display clear validation errors associated with specific fields.
*   **Submission:** Handle form submission logic within the `onSubmit` handler provided by `useForm`.
*   **Reusability:** Create reusable form input components integrated with React Hook Form's `Controller` or `register`.

## 11. Testing

*   **Unit Tests (Jest + RTL):** Test individual components (especially UI logic), custom hooks, and utility functions in isolation. Mock dependencies (API calls, hooks).
*   **Integration Tests (Jest + RTL):** Test interactions between multiple components, state management, and routing within parts of the application.
*   **End-to-End Tests (Playwright):** Test critical user flows from the user's perspective, interacting with the full application (frontend + mocked/live backend). Define key flows like login, create entry, view entry.
*   **Coverage:** Aim for meaningful test coverage (>80% for critical logic/components), focusing on functionality and edge cases. Configure coverage reports.
*   **Mocking:** Use Jest's mocking capabilities and potentially Mock Service Worker (MSW) for mocking API requests during testing.

## 12. Accessibility (a11y)

*   **Compliance:** Strive for WCAG 2.1 AA compliance.
*   **Semantic HTML:** Use appropriate HTML elements (`<button>`, `<nav>`, `<main>`, etc.).
*   **ARIA Attributes:** Apply ARIA roles and attributes correctly, especially for custom components or dynamic content updates.
*   **Keyboard Navigation:** Ensure all interactive elements are focusable and operable via keyboard alone in a logical order. Manage focus appropriately in modals and dynamic interfaces.
*   **Color Contrast:** Ensure sufficient contrast between text and background according to WCAG guidelines. Test using browser dev tools or online checkers.
*   **Screen Reader Testing:** Periodically test key flows using screen readers (NVDA, VoiceOver).
*   **Automated Testing:** Integrate accessibility checks into tests using libraries like `jest-axe`.

## 13. Performance

*   **Bundle Analysis:** Regularly analyze bundle size using `@next/bundle-analyzer`. Identify and optimize large dependencies or chunks.
*   **Code Splitting:** Leveraged automatically by Next.js App Router.
*   **Image Optimization:** Use the `next/image` component for automatic optimization, resizing, and modern format delivery.
*   **Font Optimization:** Use `next/font` for optimizing local or Google fonts.
*   **Memoization:** Apply `React.memo`, `useMemo`, `useCallback` strategically to prevent unnecessary re-renders, profiling first to identify bottlenecks.
*   **Server Components:** Maximize the use of Server Components for data fetching and rendering static content to reduce client-side JavaScript.
*   **Client Component Optimization:** Keep Client Components small and focused. Avoid fetching data directly in Client Components where possible; pass data down as props from Server Components.
*   **Web Vitals:** Monitor Core Web Vitals using Vercel Analytics or other tools.

## 14. Version Control (Git)

*   **Branching:** Use GitHub Flow (main branch + feature branches). Create branches from `main` for features/bugfixes.
*   **Commits:** Follow Conventional Commits specification (e.g., `feat:`, `fix:`, `refactor:`, `chore:`, `test:`, `docs:`). Write clear, concise commit messages.
*   **Pull Requests (PRs):** All code must be reviewed via PRs before merging to `main`. PRs should include a clear description of changes and link to relevant issues. Require passing CI checks (linting, testing).
*   **Merging:** Use squash merges or rebase merges (team preference) to maintain a clean `main` branch history.

By adhering to these guidelines, we can build a high-quality, professional, and maintainable frontend for the ReFlect Journaling App.
