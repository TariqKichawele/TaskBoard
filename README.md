# TaskBoard

A modern, full-stack team task management application with a beautiful Kanban board interface. Built with React and FastAPI, featuring Clerk authentication with organization-based multi-tenancy and role-based access control.

![React](https://img.shields.io/badge/React-19.2-61DAFB?logo=react&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128-009688?logo=fastapi&logoColor=white)
![Clerk](https://img.shields.io/badge/Clerk-Auth-6C47FF?logo=clerk&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)

---

## Features

- **Kanban Board** — Organize tasks across three columns: Pending, Started, and Completed
- **Team Collaboration** — Create organizations and invite team members
- **Role-Based Access Control** — Fine-grained permissions for Admin, Editor, and Viewer roles
- **Subscription Tiers** — Free tier with member limits, Pro tier with unlimited members
- **Real-time Updates** — Optimistic UI updates for a snappy user experience
- **Secure Authentication** — Powered by Clerk with organization support

---

## Tech Stack

### Frontend
- **React 19** — Modern React with hooks
- **Vite 7** — Lightning-fast build tool
- **React Router 7** — Client-side routing
- **Clerk React** — Authentication & organization management

### Backend
- **FastAPI** — High-performance Python web framework
- **SQLAlchemy** — SQL toolkit and ORM
- **SQLite** — Lightweight database
- **Clerk Backend API** — Server-side authentication
- **Svix** — Webhook verification

---

## Project Structure

```
taskboard/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   │   ├── KanbanBoard.jsx
│   │   │   ├── TaskCard.jsx
│   │   │   ├── TaskColumn.jsx
│   │   │   ├── TaskForm.jsx
│   │   │   └── Layout.jsx
│   │   ├── pages/            # Page components
│   │   │   ├── HomePage.jsx
│   │   │   ├── DashboardPage.jsx
│   │   │   ├── PricingPage.jsx
│   │   │   ├── SignInPage.jsx
│   │   │   └── SignUpPage.jsx
│   │   ├── services/         # API service layer
│   │   └── styles/           # CSS modules
│   └── package.json
│
├── backend/                  # FastAPI backend application
│   ├── app/
│   │   ├── api/              # API route handlers
│   │   │   ├── tasks.py
│   │   │   └── webhooks.py
│   │   ├── core/             # Core configuration
│   │   │   ├── auth.py
│   │   │   ├── clerk.py
│   │   │   ├── config.py
│   │   │   └── db.py
│   │   ├── models/           # Database models
│   │   └── schemas/          # Pydantic schemas
│   └── pyproject.toml
│
└── README.md
```

---

## Getting Started

### Prerequisites

- **Node.js** 18+ and npm
- **Python** 3.14+
- **uv** (Python package manager) — [Install uv](https://docs.astral.sh/uv/)
- **Clerk Account** — [Sign up at clerk.com](https://clerk.com)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd taskboard
```

### 2. Set Up Clerk

1. Create a new application in your [Clerk Dashboard](https://dashboard.clerk.com)
2. Enable **Organizations** in your Clerk settings
3. Create custom roles with the following permissions:
   - `org:tasks:view` — View tasks
   - `org:tasks:create` — Create tasks
   - `org:tasks:edit` — Edit tasks
   - `org:tasks:delete` — Delete tasks
4. (Optional) Set up Clerk Commerce for subscription billing

### 3. Backend Setup

```bash
cd backend

# Create environment file
cp .env.example .env  # Or create .env manually
```

Add the following to your `.env` file:

```env
CLERK_SECRET_KEY=sk_test_xxxxx
CLERK_PUBLISHABLE_KEY=pk_test_xxxxx
CLERK_WEBHOOK_SECRET=whsec_xxxxx  # Optional, for webhook verification
CLERK_JWKS_URL=https://your-clerk-instance.clerk.accounts.dev/.well-known/jwks.json

DATABASE_URL=sqlite:///./taskboard.db
FRONTEND_URL=http://localhost:5173
```

Install dependencies and run:

```bash
# Install dependencies
uv sync

# Start the server
uv run python start.py
```

The API will be available at `http://localhost:8000`

### 4. Frontend Setup

```bash
cd frontend

# Create environment file
cp .env.example .env  # Or create .env manually
```

Add the following to your `.env` file:

```env
VITE_CLERK_PUBLISHABLE_KEY=pk_test_xxxxx
VITE_API_URL=http://localhost:8000
```

Install dependencies and run:

```bash
# Install dependencies
npm install

# Start the development server
npm run dev
```

The app will be available at `http://localhost:5173`

---

## API Endpoints

### Tasks

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| `GET` | `/api/tasks` | List all tasks in organization | `org:tasks:view` |
| `POST` | `/api/tasks` | Create a new task | `org:tasks:create` |
| `GET` | `/api/tasks/{id}` | Get a specific task | `org:tasks:view` |
| `PUT` | `/api/tasks/{id}` | Update a task | `org:tasks:edit` |
| `DELETE` | `/api/tasks/{id}` | Delete a task | `org:tasks:delete` |

### Webhooks

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/webhooks/clerk` | Handle Clerk subscription events |

---

## 👥 Role-Based Access Control

TaskBoard uses Clerk's organization roles to manage permissions:

| Role | View | Create | Edit | Delete |
|------|------|--------|------|--------|
| **Admin** | ✅ | ✅ | ✅ | ✅ |
| **Editor** | ✅ | ✅ | ✅ | ❌ |
| **Viewer** | ✅ | ❌ | ❌ | ❌ |

---

## 💳 Subscription Tiers

| Feature | Free | Pro |
|---------|------|-----|
| Task Management | ✅ | ✅ |
| Organization Members | 2 | Unlimited |
| Kanban Board | ✅ | ✅ |

Subscription management is handled via Clerk Commerce webhooks.

---

## Development

### Running Tests

```bash
# Backend tests
cd backend
uv run pytest

# Frontend linting
cd frontend
npm run lint
```

### Building for Production

```bash
# Frontend build
cd frontend
npm run build

# Preview production build
npm run preview
```

---

## Environment Variables

### Backend

| Variable | Description | Required |
|----------|-------------|----------|
| `CLERK_SECRET_KEY` | Clerk secret key | Yes |
| `CLERK_PUBLISHABLE_KEY` | Clerk publishable key | Yes |
| `CLERK_WEBHOOK_SECRET` | Webhook signing secret | No |
| `CLERK_JWKS_URL` | Clerk JWKS URL for JWT verification | Yes |
| `DATABASE_URL` | SQLite database URL | Yes |
| `FRONTEND_URL` | Frontend URL for CORS | Yes |

### Frontend

| Variable | Description | Required |
|----------|-------------|----------|
| `VITE_CLERK_PUBLISHABLE_KEY` | Clerk publishable key | Yes |
| `VITE_API_URL` | Backend API URL | Yes |

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

