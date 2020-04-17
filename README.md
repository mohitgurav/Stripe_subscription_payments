# Stripe_subscription_payments

# Usage

1. Clone the repository and make it cwd.
2. Install and upgrade virtualenv package by ```pip3 install virtualenv```
3. Create virtual environment ```virtualenv venv```
4. Activate the virtal environment ```source venv/bin/activate``` for Linux and ```./venv/Scripts/activate``` for Windows.
5. Install the required libraries ```pip3 install -r requirements.txt```
6. Create a stripe account by going to https://stripe.com/
7. Get your publishable and secret test keys. Change the STRIPE_PUBLISHABLE_KEY and STRIPE_SECRET_KEY values in subscriptionsystem/settings.py.
8. Also, enter your publishable in in memberships/static/memberships/checkout.js
9. Create billing plans for your product on Stripe. You will get stripe plan id for each plan.
10. Now, create a superuser by ```python3 manage.py createuser``` and a user will be created on your stripe account.
11. Login with the credentials of created superuser at http://127.0.0.1:8000/admin
12. Under membership paste your stripe plan id fpr each .
13. Now you can subscribe to any of the plans by going to http://127.0.0.1:8000/memberships.
14. Give a star if you found this useful!
