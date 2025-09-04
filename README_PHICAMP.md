# PhiCamp Email Dashboard

A separate email collection dashboard for PhiCamp, using the `phicamp_emails` table in your existing PostgreSQL database.

## Features

- **Separate Database Table**: Uses `phicamp_emails` table instead of `trial_emails`
- **Google OAuth Integration**: Users can login with Google accounts
- **Email Collection**: Automatically saves and verifies emails
- **Dashboard Interface**: Clean, paginated dashboard to view collected emails
- **CSV Export**: Download collected emails as CSV file
- **Responsive Design**: Works on desktop and mobile devices

## API Endpoints

### Email Collection
- `POST /save_phicamp_email` - Save a new email (auto-verified)
- `POST /check_phicamp_email` - Check if email exists and is verified

### Authentication
- `GET /auth/google/login` - Initiate Google OAuth login
- `GET /auth/google/callback` - Google OAuth callback

### Dashboard
- `GET /phicampdashboard` - Dashboard login page
- `POST /phicampdashboard` - Handle dashboard login
- `GET /phicampdashboard/logout` - Logout from dashboard
- `GET /phicampdashboard/download` - Download emails as CSV

## Environment Variables

Set these environment variables in your Railway deployment:

```bash
# Database Configuration
DB_HOST=your-db-host
DB_PORT=5432
DB_NAME=wifi_hotspot
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_SSLMODE=require

# Application Configuration
SECRET_KEY=your-secret-key
BASE_URL=https://your-phicamp-dashboard.up.railway.app
DASHBOARD_PASSWORD=your-dashboard-password

# Google OAuth (optional - same as original dashboard)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

# Mikrotik Hotspot Configuration
GATEWAY_IP=172.19.20.1
HOTSPOT_USER=user
HOTSPOT_PASS=user
DST_URL=https://nuanu.com/
```

## Database Schema

The application will automatically create the `phicamp_emails` table:

```sql
CREATE TABLE phicamp_emails (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    is_verified BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Deployment on Railway

1. **Create a new Railway project**:
   - Go to [Railway.app](https://railway.app)
   - Create a new project
   - Connect your GitHub repository

2. **Configure the deployment**:
   - Set the start command: `python phicamp_app.py`
   - Add all required environment variables
   - Deploy the application

3. **Update your Mikrotik hotspot**:
   - Change the redirect URL to point to your new PhiCamp dashboard
   - Update any forms or scripts to use the new endpoints

## Key Differences from Original Dashboard

1. **Table Name**: Uses `phicamp_emails` instead of `trial_emails`
2. **Endpoint Names**: All endpoints prefixed with `phicamp_` for clarity
3. **Branding**: Updated UI with PhiCamp branding and purple color scheme
4. **CSV Filename**: Downloads as `phicamp_emails.csv`
5. **Base URL**: Configurable for separate deployment

## Usage

1. **For Email Collection**: Point your Mikrotik hotspot forms to the new endpoints:
   - `POST /save_phicamp_email` for saving emails
   - `POST /check_phicamp_email` for checking email status

2. **For Dashboard Access**: Navigate to `/phicampdashboard` and login with your password

3. **For Google OAuth**: Users can login via `/auth/google/login`

## Development

To run locally:

```bash
pip install -r requirements_phicamp.txt
python phicamp_app.py
```

The application will be available at `http://localhost:8000`

## Security Notes

- Change the default `DASHBOARD_PASSWORD` in production
- Use a strong `SECRET_KEY` for session management
- Ensure your database credentials are secure
- Consider implementing rate limiting for production use
