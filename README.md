# Team Project repo


Master: 
[![Build Status on Master](https://travis-ci.com/gcivil-nyu-org/fall2019-cs-gy-6063-team-one.svg?token=amzqTtkAvZH6KRzygZox&branch=master)](https://travis-ci.com/gcivil-nyu-org/fall2019-cs-gy-6063-team-one)
[![Coverage Status on Master](https://coveralls.io/repos/github/gcivil-nyu-org/fall2019-cs-gy-6063-team-one/badge.svg?branch=master&t=rtuHex)](https://coveralls.io/github/gcivil-nyu-org/fall2019-cs-gy-6063-team-one?branch=master)

Develop: 
[![Build Status on Develop](https://travis-ci.com/gcivil-nyu-org/fall2019-cs-gy-6063-team-one.svg?token=amzqTtkAvZH6KRzygZox&branch=develop)](https://travis-ci.com/gcivil-nyu-org/fall2019-cs-gy-6063-team-one)
[![Coverage Status on Develop](https://coveralls.io/repos/github/gcivil-nyu-org/fall2019-cs-gy-6063-team-one/badge.svg?branch=develop&t=rtuHex)](https://coveralls.io/github/gcivil-nyu-org/fall2019-cs-gy-6063-team-one?branch=develop)

Apps
- uplyft
- register
- candidate_login
- employer_login
- candidate_profile
- jobs
- apply
- applications
- password_reset

Views
- uplyft.index: 
    - Purpose: Directs anonymous users to either the candidate or employer login/registration page.
    - Additional purpose(s): When anonymous users try to perform actions of a logged in
     user, they will be redirected here.
    - Security:
        - Accessible to all users (candidates, employers, admins, anonymous users).
- candidate_login
    - Purpose: Anonymous user can input their email/password and login as a
     candidate.
     - Additional purpose(s): 
        - "Forgot your password?" link redirects to password_reset view.
     - Security: 
        - Accessible to all users.
        - Employers are not able to login through this interface. 
        - Admins are not able to login through this interface. 
- employer_login
    - Purpose: Anonymous user can input their email/password and login as an employer.
    - Security: 
        - Accessible to all users.
        - Candidates are not able to login through this interface. 
        - Admins are not able to login through this interface. 
- register.candidate_register:
    - Purpose: Anonymous user can register as a candidate. 
    - Security: 
        - Accessible to all users. 
- register.employer_register: 
    - Purpose: Anonymous user can register as an employer.
    - Security:
        - Accessible to all users. 
- candidate_profile.update_candidate_profile: 
    - Purpose: Candidate can view/update their profile details. 
    - Security: 
        - Accessible only to candidates.
         - How restricted users will be redirected: 
            - Employers: dashboard
            - Admins: admin home
            - Anonymous: uplyft:index
- jobs.JobsView
    - Purpose: Simple search bar which can be used to find a job that matches the query
    on any of the following: 
        - Job.business_title
        - Job.work_location
        - Job.department_name
    - Security: 
        - Accessible to candidates and employers. 
- jobs.JobAdvancedSearch
    - Purpose: Advanced search which can be used to find a job that matches the query
    on any of the following: 
        - Job.business_title
        - Job.work_location
        - Job.department.name
        - Job.posting_date
    - Security: 
        - Accessible to candidates and employers.
        - How restricted users will be redirected: 
            - Admins: admin home
            - Anonymous: uplyft:index
- jobs.JobDetailView
    - Purpose: Display job details for candidate/employer. Candidates can also link
     to apply to other jobs and view related jobs. Employers can also view submitted
     /accepted/rejected applications. 
        - For candidates:
            - Display the job details. 
            - If the candidate has applied and has an active application, they will
             see an alert that they've already applied with a link to the submitted
              application's details page.
            - If the candidate has NOT yet applied (or has INACTIVE application(s
            )), an "Apply" button will redirect them to apply.apply where they can
             review/edit/submit their application. 
            -@TODO: Display a count of other NEW applications submitted to this
             job, or a message "0 applications submitted - be the first!"
            -@TODO: Display suggestions of related jobs.
        - For employers: 
            - If the employer belongs to the same Department as the job: 
                - Display the job details.
                - @TODO: List of submitted applications, with a link to each application
                 details page.
                - @TODO: If a candidate has been accepted/rejected, will display a
                 breakdown of accepted/rejected candidates.
            - If the employer does NOT belong to the same Department as the job:
                - Display the job details only.
     - Security: 
        - How restricted users will be redirected: 
            - Admins: admin home
            - Anonymous: uplyft:index
- apply.apply
    - Purpose: 
        - @TODO Display a form for a candidate to complete and submit an application
        . The
     form will be prepopulated with the candidate's profile details and the
      candidate is free to change any prior to submitting. 
        - @TODO There is an option to "Update profile" or not with the submitted details, 
        and in the event that the option is checked, if any changes are made to the form
       prior submission, those changes are also reflected in the profile (as long as
        they still meet the constraints of the underlying Application, CandidateProfile, 
        and CustomUser models).
    - Security: 
        - Accessible to candidates. 
        - How restricted users will be redirected: 
            - Employers: dashboard
            - Admins: admin home
            - Anonymous: uplyft:index
- 

Models
-


Forms 
-


Typical Uses
-


Tests
- Django tools utilized in the test suite: 
- Coverage
