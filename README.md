# UserInfoDataEntryForm

A local Python Tkinter application for entering user information through a graphical form. Submitted data is printed to the console and saved to a local SQLite database.

## Features

- Desktop graphical interface built with Tkinter
- Collects user and registration information
- Validates that first name, last name, email, and terms acceptance are provided
- Prints submitted entries to the console
- Saves records locally to an SQLite database
- Automatically creates the `persona_data` table if it does not already exist
- Does not require an internet connection

## Information Stored

The form can collect and store:

- First name
- Last name
- Email address
- Title
- Age
- Nationality
- Street address
- City
- State
- ZIP code
- Registration status
- Number of degrees
- Number of children
- Graduation status, if enabled in the application

## Requirements

- Python 3
- Tkinter support in your Python installation
- SQLite support, included with standard Python installations

No external Python packages are required.

## Database

The application creates a SQLite database file named:

```text
data.db
```

The file is created in the directory where the script is run. It contains a table named:

```text
persona_data
```

Each successful form submission adds a new row to that table.

### Viewing Saved Records

You can inspect the database using the SQLite command-line tool:

```bash
sqlite3 data.db
```

Then run:

```sql
SELECT * FROM persona_data;
```

Exit SQLite with:

```sql
.quit
```

## Project Structure

```text
UserInfoDataEntryForm/
├── main.py
├── data.db                 # Created after the first successful submission
├── README.md
├── LICENSE.md
├── SECURITY.md
└── PRIVACY.md

```

## Privacy

All form data is processed locally. The application prints submitted information to the local console and stores it in the local `data.db` SQLite database.

It does not intentionally transmit data to the developer, use analytics, or upload records to an external service. See [PRIVACY.md](PRIVACY.md) for full details.

## Source Availability

This repository is published for display and personal educational review only.
Running, copying, modifying, redistributing, or deploying the source code is
not permitted without prior written permission. See [LICENSE.md](LICENSE.md).

## License

This source code is provided under the
[Display and Educational Use License](LICENSE.md).

You may view the repository for personal, non-commercial educational purposes
only. You may not copy, run, modify, redistribute, deploy, or use this code in
another project without prior written permission from the copyright holder.

© 2026 Eddie Menard. All rights reserved.ata-entry and educational purposes. You are responsible for obtaining permission to collect, store, and manage any personal information entered into the form.