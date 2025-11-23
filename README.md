Jules Ops CLIJules Ops is a unified command-line tool that bridges Jules AI sessions with GitHub project management. It allows you to visualize your development status in one place and seamlessly turn GitHub Issues into active AI coding sessions.🚀 Key FeaturesUnified Dashboard: See active Jules sessions, open Pull Requests, and assigned Issues in a single view.Smart Start (work-on): Instantly start a Jules session from a GitHub Issue ID. The tool automatically fetches the issue title/body and creates a dedicated feature branch.Workflow Automation: Manage the lifecycle of AI sessions (Create → Watch → Publish PR) without leaving the terminal.Zero-Config Client: Embedded client logic means no external Python dependencies other than requests.🛠️ PrerequisitesPython 3.xGitHub CLI (gh)Must be installed and authenticated (gh auth login).Python Requests Librarypip install requests
⚙️ SetupMake the script executable:chmod +x jules_ops.py
Set your API Key:You can export it as an environment variable (recommended) or pass it via flags.export JULES_API_KEY="your-api-key-here"
📖 Usage Guide1. The Dashboard (status)This is your "Mission Control". It displays:🧠 Jules Sessions: Active/Succeeded AI tasks.🚀 Pull Requests: Open PRs with their review status (✅ Approved, 🚫 Changes Requested).📢 Issues: Your open backlog../jules_ops.py status
2. The "Smart Start" Workflow (work-on)The fastest way to start coding. Pick an issue ID from the status board and let Jules handle it.Command:./jules_ops.py work-on <issue_id>
What happens:Fetches Issue #102 title and description from GitHub.Creates a target branch (e.g., feature/issue-102).Sends a prompt to Jules with the issue context.Starts monitoring the session.3. Manual Session Creation (create)For tasks not tracked in GitHub or quick experiments../jules_ops.py create --prompt "Refactor the login page to use NextAuth" --branch "refactor/login" --title "Login Refactor"
4. Publish a PR (publish)When a session succeeds, tell Jules to finalize the work and open a Pull Request../jules_ops.py publish <session_name_or_id>
5. Monitoring (watch)Re-attach to a running session to see live status updates../jules_ops.py watch <session_name_or_id>
⚡ Workflow ExampleHere is a typical developer workflow using Jules Ops:Check the board:./jules_ops.py status
# You see Issue #45: "Fix memory leak in websocket hook"
Start work:./jules_ops.py work-on 45
# Jules starts analyzing the issue and writing code...
Wait for success:The CLI monitors the session until it reports SUCCEEDED.Publish:./jules_ops.py publish projects/123/locations/us/sessions/abc-xyz
# Jules creates the PR.
Verify:./jules_ops.py status
# You now see a new Open PR linked to branch 'feature/issue-45'
