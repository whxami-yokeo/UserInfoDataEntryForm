# Privacy Policy

**Last updated:** August 23, 2026

## Overview

UserInfoDataEntryForm is a local Python application that lets users enter personal and registration-related information through a graphical form.

The application prints submitted information to the local console and saves it to a local SQLite database file named `data.db` in the directory where the script is run. It does not operate a hosted service, use analytics, or send form data to the developer or other third parties.

## Information Collected

The form may collect information entered directly by the user, including:

- First name
- Last name
- Email address
- Title
- Age
- Nationality
- Street address
- City, state, and ZIP code
- Registration status
- Number of degrees
- Number of children
- Graduation status, if enabled in the form

The user decides which information to enter. However, first name, last name, and email address are required before the application saves a record.

## How Information Is Used

The application uses the submitted information only to:

- Display the entered information in the local console for the current user.
- Save the entered information in the local SQLite database.
- Maintain local records created through the form.

The application is not intended to transmit, analyze, profile, market, sell, or otherwise share submitted information.

## Local Storage

Submitted form data is stored locally in an SQLite database file called `data.db`.

The database is created in the local directory from which the script runs, unless the application code is changed to use another location. The database may contain records with the information listed in the **Information Collected** section.

The application may also cause data to appear in local locations outside the database, including:

- The terminal or IDE console where the script is run
- Terminal scrollback or command history, depending on the user’s environment
- Operating-system backups
- IDE logs, crash reports, or temporary files
- Copies of the project folder or database file

## Data Sharing

UserInfoDataEntryForm does not:

- Send form data over the internet.
- Send data to the developer.
- Upload the database to a cloud service.
- Use analytics, advertising, telemetry, or tracking tools.
- Sell, rent, disclose, or share personal information with third parties.

Any sharing caused by the user’s own device configuration—such as cloud backup, synced folders, shared drives, or source-control repositories—is outside the application’s control.

## Data Retention and Deletion

Form records remain in `data.db` until they are deleted by the user or removed by another local process.

To remove locally stored records, users may:

- Delete individual records using an SQLite database tool or a feature added to the application.
- Delete `data.db` to remove the entire local database and all saved form entries.
- Clear the terminal or console output if submitted information was printed there.

Deleting the database is permanent unless a backup exists.

## Security

The application stores data locally, but local storage is not automatically secure. Anyone with access to the computer or the project directory may be able to view, copy, modify, or delete the database file and console output.

Users should:

- Run the application only on a device they trust.
- Restrict access to the project directory and `data.db`.
- Avoid placing the database in publicly shared or version-controlled folders.
- Do not commit `data.db` to Git or other source-control systems.
- Use device-level protections such as account passwords and disk encryption where appropriate.
- Be cautious when entering sensitive personal information.

## Third-Party Services

UserInfoDataEntryForm does not intentionally use third-party online services to process form data.

The application relies on Python and its included modules, including Tkinter for the graphical interface and SQLite for local database storage. Those components operate locally as part of the user’s Python environment.

## User Responsibilities

Users are responsible for:

- Ensuring they have permission to collect and store the information entered into the form.
- Protecting the computer and directory where the database is stored.
- Managing backups, synced folders, console output, and copies of `data.db`.
- Reviewing and modifying the source code if different privacy, retention, encryption, or access-control requirements apply.
- Complying with applicable privacy laws and organizational policies.

## Changes to This Policy

This Privacy Policy may be updated if the application’s functionality or data-handling practices change. The “Last updated” date at the top of this document will reflect the most recent revision.

## Contact

For questions or concerns about this Privacy Policy, open an issue in the UserInfoDataEntryForm repository or contact the project maintainer through the contact method listed in the repository.