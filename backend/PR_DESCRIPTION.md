# Pull Request: Update User Endpoints and Schemas for Portfolio and User

## Description

This pull request includes the following changes:

- Updated the `user_endpoints.py` file to handle user creation and updates correctly.
- Modified the `PortfolioCreate` schema in `schemas/portfolio.py` to include a `user_id` field.
- Updated the `UserCreate` schema in `schemas/user.py` to replace the `hashed_password` field with a `password` field to accept plain text passwords.
- Added password hashing logic using the `passlib` library in the `create_user` endpoint.
- Corrected the handling of the `portfolio` parameter in the `create_portfolio` function within `portfolio_crud.py`.

## Changes

### `user_endpoints.py`
- Updated the `create_user` function to hash the password and remove the plain password from the user data dictionary before creating the user.
- Updated the `update_user` function to handle the `user` parameter as a dictionary, accessing values using key notation and conditionally updating the `hashed_password` field.

### `schemas/portfolio.py`
- Added a `user_id` field of type `uuid.UUID` to the `PortfolioCreate` schema.

### `schemas/user.py`
- Replaced the `hashed_password` field with a `password` field in the `UserCreate` schema to accept plain text passwords.

### `portfolio_crud.py`
- Corrected the handling of the `portfolio` parameter in the `create_portfolio` function to ensure the `user_id` field is correctly processed.

## Testing

- Tested the `GET /api/v1/users/` endpoint locally using cURL commands.
- Tested the `POST /api/v1/users/` endpoint locally using cURL commands.
- Tested the `PUT /api/v1/users/{user_id}` endpoint locally using cURL commands.
- Tested the `GET /api/v1/portfolios/` endpoint locally using cURL commands.
- Tested the `POST /api/v1/portfolios/` endpoint locally using cURL commands.
- Tested the `PUT /api/v1/portfolios/{portfolio_id}` endpoint locally using cURL commands.

All endpoints have been tested and are functioning correctly.

## Deployment

- The changes have been pushed to the `update-env-credentials` branch.
- The deployment process will be triggered automatically upon merging this pull request.
- The project URL on Railway should be used to verify the deployment status and ensure the application is running correctly.

## Link to Devin run

https://staging.itsdev.in/devin/61e56c34f4f44cafb679fb63f2c5a6fa

Please review the changes and provide feedback.

Thank you!
