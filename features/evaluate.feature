
Feature: showing off behave
    Scenario: Evaluate John Doe
        Given I am evaluating a resume
        When I evaluate the resume of John Doe
        Then the applicant should have technical skills
        And the applicant should know the Java language
        And the applicant should have web experience
