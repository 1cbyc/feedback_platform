# feedback platform

this should be the fastest and easiest way to get feedback on your projects as a developer.

i think i need to sleep fuckk! just lost $62k trading


## WHAT I WANT TO IMPLEMENT

1. User Authentication: to allow users to create accounts and log in to submit feedback.
2. Feedback Submission Forms: creating customizable forms for collecting feedback, including rating systems and open-ended questions.
3. Dashboard for Users: making a ui where feedback providers can view their submitted feedback and any responses.
4. Admin Dashboard: a small backend interface for admins (esp myself) to manage feedback, analyze trends, and generate reports.
5. Notifications: an email and also in-app notifications for feedback responses or important updates.
5. Data Export: well, considering options to download feedback data in formats like CSV or Excel.

## TECH STACK

1. Front-End: HTML, CSS, JavaScript/Typescript (considering using the opportunity to master reactjs)
2. Back-End: considering using Python (Flask), i am not using PHP because i intentionally didn't setup PHP on my third mac (this one), i use this one for ML shii
3. Database: still thinking between MySQL or PostgreSQL for storing feedback and user information
4. Deployment: I would use Railway to hosting the web app (yes, it is pr for Railway, fuck vercel, brimble and all)

## THIS IS MY DB DESIGN (in case i forget again)

for users table:

    id
    username
    email
    password_hash

for feedback table:

    id
    user_id (foreign key referencing Users)
    feedback_text
    rating (optional)
    created_at
    updated_at


## FUCKKKKK
something tells me i might have to become a ui designer for this, because there is this guy i could've asked to make a ui for me, but he might stress me.

