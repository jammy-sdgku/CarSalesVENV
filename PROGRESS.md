# CarSales Progress

Updated: 9 November 2026

## Project overview

Django vehicle inventory application using MongoDB Atlas.
Vehicle records contain ID, Name, Year, and Price.

## Implemented in the current code

### Database connection
- Replaced the localhost MongoDB connection with an environment variable.
- Connection URI is read from `carsalesClient`.
- Django settings load the root `.env` file using python-dotenv.
- A shared MongoClient is reused across requests.
- Credentials are not embedded in the view.

### Dependencies
- Created requirements.txt with pinned installed versions.
- Includes Django, PyMongo, dnspython, and python-dotenv.

### Vehicle management
- Vehicle listing reads records from MongoDB.
- Add vehicle validates input before inserting.
- Invalid additions preserve submitted values and display form errors.
- Existing edit functionality updates vehicle details.

### Price and year formatting
- Prices display with thousands separators and no decimal places.
- IDs and years explicitly use unlocalized formatting.
- Price form field uses localized numeric validation.
- Prices remain numeric in MongoDB; display rounding does not change stored data.

### User interface
- Listing and add/edit pages share a responsive stylesheet.
- Added navigation, styled tables, buttons, form fields, and an empty state.
- Both pages load CSS through Django static tags.
- STATIC_URL and STATIC_ROOT are configured.

### Vehicle deletion
- Delete button asks for confirmation using the vehicle name.
- Deletion requires POST and includes CSRF protection.
- Success message is queued only when a record is deleted.
- A missing-record message is shown when no matching vehicle exists.
- Listing template renders Django messages after redirecting.

## Follow-up items

- Browser-test listing, adding, editing, and deleting against Atlas.
- Verify comma-separated price input is accepted with current locale settings.
- Verify Cancel prevents deletion and confirmed deletion displays feedback.
- Improve edit validation: invalid submissions currently redirect without errors.
- Handle editing a vehicle that no longer exists.
- Align branding: listing says "JJIT Car Sales App"; form says "CarSales".
- Consider moving deletion messages above the inventory for better visibility.
- Confirmation currently depends on JavaScript.
- Confirm `.env` is excluded from version control.
- Configure production static-file serving when deploying.

## Verification status

Progress above is based on inspection of current source files.
No automated tests, browser tests, or live database checks were run
during this documentation review.