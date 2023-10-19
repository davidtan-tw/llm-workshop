
Feature: showing off behave
    Scenario: Evaluate a developer resumue
        Given I am looking for a developer
        When I evaluate the resume of John Doe
        Then the resume needs to have the right technical skills for a developer
