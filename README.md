# Welcome to the test for Technical Support Engineer at Climapulse!

## Repository setup

#### Setup your own repository

After receiving the technical-support-test.zip file you can transform it into your own new (private or public) Github repository. Push the code given in the zip file into your main branch as-is.

#### Submit your solution

Please submit your solution as a PR inside your own repository to simplify and speed up the review process. After you have written your solution, provide us the link to your own repository (and access if applicable).

## Application setup

#### Run the Docker setup

    $ docker-compose up --build -d

#### Simulate withdrawing refrigerant from a vessel:

    $ docker-compose run web python manage.py withdraw

## The problem

We have a refrigerant vessel with a starting content of 50 Kg. Our withdraw script simulates two users entering a 10 Kg withdrawal on the same vessel.

However, it seems that only one of those is being registered as the vessel is being emptied by 10 Kg on each run instead of the expected 20 Kg. Can you find the bug and solve it?

## Bonus - Useability upgrade

Currently, even if the vessel is empty, users can still attempt to withdraw from it, resulting in a database exception. Although our database schema prevents negative values, we aim to enhance user experience by displaying a clearer message in the withdrawal script. This message should notify users that the vessel is empty and further withdrawals are not possible. Can you improve the useability of this script?

Happy debugging!
