The project is a real-time heart rate monitoring dashboard built with Next.js, Material-UI, WebSockets, and Spotify integration. It features a custom Express server (`server.ts`) that manages a persistent WebSocket server and background services, making it a stateful application. The application is designed to be deployed on a traditional Node.js host and is not compatible with serverless platforms.

The frontend is built with React and Material-UI, and it receives real-time updates from the server via WebSockets. The main dashboard displays a timer, heart rate tiles, a Spotify player, and an embedded Google Doc.

The backend is a custom Express server that handles the Next.js application, the WebSocket server, and several services, including a Tabata timer and a Spotify polling service.

### Building and Running

#### Development

To run the application in development mode, use the following command:

```bash
npm run dev
```

This will start the Next.js application, the WebSocket server, and all background services. The application will be available at `http://127.0.0.1:3000`.

#### Production

To build and run the application in production, use the following commands:

```bash
# Build the Next.js app and the custom server
npm run build

# Start the application with PM2
npm run start
```

### Development Conventions

*   **State Management:** All global state is managed by the server and pushed to clients via WebSockets. Client-side state should be ephemeral.
*   **UI Components:** Use Material-UI (MUI) for all components.
*   **Code Quality:** Run `npm run lint` to check for linting errors before committing changes.
*   **Testing:** The project uses Jest for unit tests and Playwright for end-to-end and visual regression testing.
    *   Run unit tests with `npm run test:unit`.
    *   Run Playwright tests with `npm run test:visual`.
*   **Custom Server:** Always use `npm run dev` for development to ensure all background services are running.

### Testing Philosophy

To save costs, this project avoids running automated tests on GitHub Actions. Instead, a local testing process is enforced. All tests should be run locally before pushing changes. The `hrm-workspace` repository contains scripts to replicate the local testing process that was established in the `hrm` repository.
