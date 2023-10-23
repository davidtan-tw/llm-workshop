
Feature: Extract correct skills from resume
    Scenario: Evaluate John Doe
        Given I am evaluating a resume
        When I evaluate the resume of John Doe
        Then they should have technical skills
        And they should know the Java language
        And they should have web experience
