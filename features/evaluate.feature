
Feature: showing off behave
    Scenario: Evaluate a Java developer resumue
        Given I am looking for a Java developer
        When I evaluate the resume of John Doe
        Then the resume needs to have the Java language
        And the resume needs to have web experience
