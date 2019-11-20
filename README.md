# Team Project repo


Master: 
[![Build Status on Master](https://travis-ci.com/gcivil-nyu-org/fall2019-cs-gy-6063-team-one.svg?token=amzqTtkAvZH6KRzygZox&branch=master)](https://travis-ci.com/gcivil-nyu-org/fall2019-cs-gy-6063-team-one)
[![Coverage Status on Master](https://coveralls.io/repos/github/gcivil-nyu-org/fall2019-cs-gy-6063-team-one/badge.svg?branch=master&service=github)](https://coveralls.io/github/gcivil-nyu-org/fall2019-cs-gy-6063-team-one?branch=master&service=github)

Develop: 
[![Build Status on Develop](https://travis-ci.com/gcivil-nyu-org/fall2019-cs-gy-6063-team-one.svg?token=amzqTtkAvZH6KRzygZox&branch=develop)](https://travis-ci.com/gcivil-nyu-org/fall2019-cs-gy-6063-team-one)
[![Coverage Status on Develop](https://coveralls.io/repos/github/gcivil-nyu-org/fall2019-cs-gy-6063-team-one/badge.svg?branch=develop&service=github)](https://coveralls.io/github/gcivil-nyu-org/fall2019-cs-gy-6063-team-one?branch=develop&service=github)

## Maintenance


### Demo users

Follow the following steps to reset candidates/employers in the database:

1. in the terminal, launch Django's Python REPL environment:

```% python3 manage.py shell```

2. in Python REPL:

To create demo users, and skip for any existing demo user:

```>>> from maintenance_worker import manage_demo_users; manage_demo_users.create_demo_employers()```

or

```>>> from maintenance_worker import manage_demo_users; manage_demo_users.create_demo_candidates()```

To reset demo users, discarding any current user:

```>>> from maintenance_worker import manage_demo_users; manage_demo_users.reset_demo_employers()```

or

```>>> from maintenance_worker import manage_demo_users; manage_demo_users.reset_demo_candidates()```

3. check your database for the changes.

### Jobs and Departments

1. in the terminal, launch Django's Python REPL environment:

```% python3 manage.py shell```

2. in Python REPL:

```>>> from maintenance_worker import manage_jobs; manage_jobs.load_jobs()```

3. check your database for the changes.

*Limitation:* job loading script currently check duplicate records in `Department` table but not the `Job` table. Therefore, running this command multiple times may result in excessive records in the database.
