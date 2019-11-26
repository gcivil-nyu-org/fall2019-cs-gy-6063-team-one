## Set-Up Instructions
- We have not created test accounts for you. Instead, please register through the website. After you register, you will be asked to activate your account via email. An email will be sent to the email address you provided in your registration.
- Once you have activated your account, you can log in and start using UpLyft. To thoroughly test the application, you will want to create both a candidate and an employer account.
- Note: **You cannot use the same email address for your candidate and employer accounts**
**Uplyft**
- Welcome to Uplyft! We&#39;re here to help you build a career in city government. There are a wealth of opportunities for people who want to improve their communities and make an important difference in the lives of their fellow New Yorkers. We&#39;re also on a mission to help the City of New York recruit top talent
- If you&#39;re new to the site, click the button that applies to you (either Candidate or Employer) and you&#39;ll be taken to a form where you can register or log in
- If you need to return to the home page at any time, you can just click where it says &quot;Uplyft&quot; on the top left of the page

# Views
## Login Views
### Candidate Login
- Purpose: Log candidates into Uplyft.
- Accessible to: All users (Candidates, Employers, and Anonymous users)
- Features:
  - Login form
  - **&quot;Forgot Password?&quot;** links to _Password Reset_ page
  - ** Sign in with Google**
  - **&quot;First time on Uplyft? Register&quot;** redirects new users to the _Candidate Registration_ page
  - **&quot;Employer? Login here&quot;** redirects employers to the _Employer Login_ page.
- Notes:
  - A candidate will not be able to submit the form until both required fields (email and password) are provided.
  - If a candidate provides invalid credentials, they will receive an error message.
  - If an employer tries to login through this page, they will receive a hint to login through the _Employer Login_ page.

### Employer Login
- Purpose: Log employers into Uplyft.
- Accessible to: All users (Candidates, Employers, and Anonymous users)
- Features:
  - Login form
  - **&quot;Forgot Password?&quot;** links to _Password Reset_ page
  - **&quot;First time on Uplyft? Register&quot;** redirects new users to the _Employer Registration_ page
  - **&quot;Candidate? Login here&quot;** redirects candidates to the _Candidate Login_ page.
- Validation
  - The employer will not be able to submit the form until both fields (email and password) are filled.
  - If the employer provides invalid credentials, they will receive an error message
  - If an employer tries to login through this page, they will receive a hint to login through the _Candidate Login_ page.

## Register Views
### Candidate Registration
- Purpose: Register candidates.
- Accessible to: All users (Candidates, Employers, and Anonymous users)
- Notes:
  - The user will not be able to submit the form until all required fields are provided:
    - first name
    - last name
    - email: validated against existing users before new user is created
    - password
  - Email authentication is required before a new candidate can login to their account. Prior to email authentication, new accounts are inactive and attempts to log in before authenticating will be unsuccessful.

### Employer Registration
- Purpose: Register employers.
- Accessible to: All users (Candidates, Employers, and Anonymous users)
- Notes:
  - The user will not be able to submit the form until all required fields are provided:
    - first name
    - last name
    - email: validated against existing users before new user is created
    - password
    - department: options are based on existing departments in the database
  - Email authentication is be required before a new employer can login to their account. Prior to email authentication, new accounts are inactive and attempts to log in before authenticating will be unsuccessful.

## Dashboard
  - Dashboard is similar to both the candidate and the employer.
  - For both the user types, there are three types of application overviews shown - "Pending", "Rejected" and "Accepted"
  - Clicking on any of these overviews will take you to an applications listing page, which will contain the list of applications for the specific application types mentioned above. You can also search for First name, last name or Title of the job in the application.
  - If there are many applications, the applications will be paginated in sets of 10.
  - If you are logged in as a candidate, you should be able to see **ONLY** your applications.
  - If you are logged in as an employer, you should be able to see **ONLY** applications that belong to the department you belong to.

## Candidate Profile
- Accessible to Candidates only.
  - Each candidate can access only their own profile.
  - The navigation bar has a button, &quot;My Profile&quot;, which can be used to access the profile and is only visible to Candidates.
- Primary feature: Enable candidate to view and update their profile information.
- Information collected:
  - First name, Last name: Must be non-numeric.
  - Email: The email must be a valid email address and cannot match the email of any existing user.
  - Portfolio website: The url must begin with a valid protocol (e.g. [http://example.com](http://example.com))
  - Resume: Required. Accepted file types are restricted to .pdf, .doc, and .docx.
  - Cover letter: Optional. Accepted file types are restricted to .pdf, .doc, and .docx.
  - Demographics (gender, race, ethnicity), health conditions, veteran status


## Job Search
- Accessible to Candidates or Employers.
- Purpose:
  - Enable users to search for available job postings.
  - Users may search by:
    - business title (e.g. Lead Application Developer)
    - department (e.g. Law Department)
    - work location (e.g. Brooklyn)
  - Search results will return a set of job cards:
    - Users may click on any of the job cards to navigate to the Job Details page for that particular job.
    - Candidates ONLY will also see additional information:
      - If the candidate has already applied to this job, they will see the status &quot;Applied&quot;.
      - If the candidate has not yet applied to this job, they will see a link to &quot;Apply Now&quot;.

## Job Details
- Purpose:
  - Provide users with details about a job posting.
Notes:
  - Allow Candidates to Redirect to an application form, or if they have already applied, to the application details page for their submitted application.
  - Accessible to Candidates and Employers, although with different functionality. Candidates have the additional option to apply or view their submitted application.
  - Contains hyperlinks back to the Department which posted this job.

## Department Details:
- On the Department Details page, you can see all of the job openings available at that department. For each job opening we provide:
  - Job ID (with a hyperlink in case the job title interests you and you want to apply)
  - Job Title
  - When the job was posted
  - Number of applications submitted
- Notes:
  - When you visit the detailed version of a job listing, you&#39;ll notice the name of the department is hyperlinked. Clicking that hyperlink will take you to the _Department Details_ page for that particular department
  - **FYI:** The Department Details page shows the same information regardless of whether you are logged in as a candidate or an employer. (The only additional item is when you&#39;ve logged in as an employer and you&#39;re looking at your own department&#39;s details page, then there is an option to edit the details)

## Apply
- Purpose: Allow a candidate to submit an application for a particular job posting.
- Accessible to Candidates only.
- Notes:
  - Candidate will be asked to update their profile details prior to submitting the application. The application form will be pre-populated with any all of the candidate's existing profile details. Candidates are then free to update their cover letter or any of the other fields, before submitting.
  - There is an option, "Update profile", that when checked will update the candidate's active profile with the submitted details.
  - Once a candidate has applied to a job, they will not be able to immediately apply again. Their application will move to the PENDING status and will go into the Pending applications list of every employer who belongs to the department which posted the job.

## Application Details
- Purpose: Provides all of the details of a submitted application, which include summary information about the job and the profile details of the applicant.
- Accessible to the Candidate who submitted the application and any Employer who belongs to the department that corresponds to this application.
- Any unauthorized Candidates or Employers will be redirected to a 403 forbidden page.


## Department Profile
- When you log in as an Employer, you&#39;ll see that there is a _Department Profile_ as one of the options in your navigation bar (next to _Jobs_ and _Log out_)
- If you click on the Department Profile, it will take you to a form for your department where you can fill out important information that you may want to share with job applicants/candidates
- The information an Employer can include in their Department Profile is:
  - Address (Headquarters or Main Office)
  - Description (Brief Explanation of your department)
  - Website (For candidates to find out more about your department)
  - Phone (For candidates to contact you)
  - Email (For candidates to contact you)
- All of these fields are optional so you may leave them blank as well
- If you update one of the fields in your department profile and click &quot;Save Changes&quot;, you will be redirected to your Department Details page, where the newly added information appears
- That information will now be visible to anyone who visits your Department Details page (that includes candidates **and** employers) until you change/update it again
- As you&#39;d expect, the only way you can change the Department Profile for a Department X is to be logged as an Employer from that department
