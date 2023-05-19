Feature: Google translate
  As a web user
  I want to use Google Translate
  to translate words between different languages

  Scenario Outline: Translate from source language to target language
    Given that user want to use the page Google_translate
    When he select the source language as <Source>
    And select the target language as <Target>
    And write the sentence <Sentence>
   Then the screen should display the <translated sentence>
    Examples:
      | Source | Target | Sentence                     |translated sentence          |
      |Spanish |English |Hola Farid!!, eres un estupido|Hi Farid !!, You are a stupid|
