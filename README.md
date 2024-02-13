# Text Anonymization and Processing with Presidio and OpenAI GPT

## Description

This project includes a Python script that integrates Microsoft Presidio for text anonymization and OpenAI's GPT for advanced text processing. It ensures sensitive information is anonymized before processing and then accurately deanonymized in the output.

## Installation

1. Clone this repository to your local machine.
2. Ensure Python 3.6+ is installed.
3. Install the required dependencies:
4. Set your OpenAI API key as an environment variable:


## Usage

Run the script from the command line, specifying the path to the text file you want to process, the language of the text (currently only 'en' is supported), and your OpenAI API key:


## Example

**Initial text : ** 

Given a text file `test.txt` with the following content:
*Jean-Philippe Patouchili, un explorateur intrépide et rêveur, menait une vie hors du commun. Né le 12 mars 1980 à Marseille, il partit très jeune à l'aventure, traversant des contrées lointaines. En 2005, il découvrit un petit village caché dans les Alpes suisses, Zermatt, où il se lia d'amitié avec un guide local, Henri, et une scientifique passionnée de botanique, Élodie. Ensemble, ils partagèrent de nombreuses expéditions, notamment l'ascension du Mont Cervin en été 2010 et une exploration dans la forêt amazonienne en 2015. Jean-Philippe était aussi un écrivain talentueux, publiant ses récits de voyage chez un petit éditeur parisien, Les Éditions du Globe, en 2018. Sa vie était un tissu d'aventures, de rencontres enrichissantes et de découvertes fascinantes.*

**Anonymized Text : **

*<PERSON_0_24>, un explorateur <PERSON_41_50> et rêveur, menait une vie hors du commun. Né le 12 <DATE_TIME_102_111> à <LOCATION_114_123>, <PERSON_125_158>, <IN_PAN_160_170> <PERSON_171_194>. <DATE_TIME_196_203>, il découvrit un petit village caché dans les Alpes suisses, <LOCATION_265_303> guide local, <PERSON_317_322>, et une scientifique <PERSON_344_367>, <PERSON_369_375>. Ensemble, ils partagèrent de <IN_PAN_406_416> expéditions, notamment l'ascension du Mont Cervin en été <DATE_TIME_474_478> et une exploration dans la forêt amazonienne en <DATE_TIME_527_531>. <PERSON_533_581>, publiant ses récits de voyage chez un petit éditeur parisien, Les Éditions du Globe, en <DATE_TIME_671_675>. <PERSON_677_692> tissu d'aventures, <LOCATION_712_740> et de découvertes fascinantes.*

**Response from OpenAI GPT : **

*<PERSON_0_24>, an explorer <PERSON_41_50> and dreamer, led an extraordinary life. Born on the 12th <DATE_TIME_102_111> in <LOCATION_114_123>, <PERSON_125_158>, <IN_PAN_160_170> <PERSON_171_194>. On <DATE_TIME_196_203>, he discovered a hidden village in the Swiss Alps, got acquainted with a local guide, <PERSON_317_322>, and a scientist <PERSON_344_367>, <PERSON_369_375>. Together, they embarked on a range of exhilarating expeditions, such as the ascent of the Matterhorn during the summer of <DATE_TIME_474_478> and an exploration into the Amazon rainforest in <DATE_TIME_527_531>. <PERSON_533_581>, subsequently published his travelogues with a small Parisian publisher, Les Éditions du Globe, in <DATE_TIME_671_675>. His works replete with thrilling adventures, breathtaking <LOCATION_712_740>, and fascinating discoveries.*

**Verifying analysis results integrity for deanonymization : **

*{'analysis_explanation': None, 'end': 24, 'entity_type': 'PERSON', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 0}, {'analysis_explanation': None, 'end': 50, 'entity_type': 'PERSON', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 41}, {'analysis_explanation': None, 'end': 111, 'entity_type': 'DATE_TIME', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 102}, {'analysis_explanation': None, 'end': 123, 'entity_type': 'LOCATION', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 114}, {'analysis_explanation': None, 'end': 158, 'entity_type': 'PERSON', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 125}, {'analysis_explanation': None, 'end': 194, 'entity_type': 'PERSON', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 171}, {'analysis_explanation': None, 'end': 203, 'entity_type': 'DATE_TIME', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 196}, {'analysis_explanation': None, 'end': 303, 'entity_type': 'LOCATION', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 265}, {'analysis_explanation': None, 'end': 322, 'entity_type': 'PERSON', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 317}, {'analysis_explanation': None, 'end': 367, 'entity_type': 'PERSON', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 344}, {'analysis_explanation': None, 'end': 375, 'entity_type': 'PERSON', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 369}, {'analysis_explanation': None, 'end': 478, 'entity_type': 'DATE_TIME', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 474}, {'analysis_explanation': None, 'end': 531, 'entity_type': 'DATE_TIME', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 527}, {'analysis_explanation': None, 'end': 581, 'entity_type': 'PERSON', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 533}, {'analysis_explanation': None, 'end': 675, 'entity_type': 'DATE_TIME', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 671}, {'analysis_explanation': None, 'end': 692, 'entity_type': 'PERSON', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 677}, {'analysis_explanation': None, 'end': 740, 'entity_type': 'LOCATION', 'recognition_metadata': {'recognizer_identifier': 'SpacyRecognizer_139694205667696', 'recognizer_name': 'SpacyRecognizer'}, 'score': 0.85, 'start': 712}, {'analysis_explanation': None, 'end': 24, 'entity_type': 'IN_PAN', 'recognition_metadata': {'recognizer_identifier': 'InPanRecognizer_139694205667168', 'recognizer_name': 'InPanRecognizer'}, 'score': 0.05, 'start': 14}, {'analysis_explanation': None, 'end': 170, 'entity_type': 'IN_PAN', 'recognition_metadata': {'recognizer_identifier': 'InPanRecognizer_139694205667168', 'recognizer_name': 'InPanRecognizer'}, 'score': 0.05, 'start': 160}, {'analysis_explanation': None, 'end': 194, 'entity_type': 'IN_PAN', 'recognition_metadata': {'recognizer_identifier': 'InPanRecognizer_139694205667168', 'recognizer_name': 'InPanRecognizer'}, 'score': 0.05, 'start': 184}, {'analysis_explanation': None, 'end': 354, 'entity_type': 'IN_PAN', 'recognition_metadata': {'recognizer_identifier': 'InPanRecognizer_139694205667168', 'recognizer_name': 'InPanRecognizer'}, 'score': 0.05, 'start': 344}, {'analysis_explanation': None, 'end': 416, 'entity_type': 'IN_PAN', 'recognition_metadata': {'recognizer_identifier': 'InPanRecognizer_139694205667168', 'recognizer_name': 'InPanRecognizer'}, 'score': 0.05, 'start': 406}, {'analysis_explanation': None, 'end': 581, 'entity_type': 'IN_PAN', 'recognition_metadata': {'recognizer_identifier': 'InPanRecognizer_139694205667168', 'recognizer_name': 'InPanRecognizer'}, 'score': 0.05, 'start': 571}*

**Final Text : **

*Jean-Philippe Patouchili, an explorer intrépide and dreamer, led an extraordinary life. Born on the 12th mars 1980 in Marseille, il partit très jeune à l'aventure, traversant des contrées lointaines. On En 2005, he discovered a hidden village in the Swiss Alps, got acquainted with a local guide, Henri, and a scientist passionnée de botanique, Élodie. Together, they embarked on a range of exhilarating expeditions, such as the ascent of the Matterhorn during the summer of 2010 and an exploration into the Amazon rainforest in 2015. Jean-Philippe était aussi un écrivain talentueux, subsequently published his travelogues with a small Parisian publisher, Les Éditions du Globe, in 2018. His works replete with thrilling adventures, breathtaking de rencontres enrichissantes, and fascinating discoveries.*


## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your improvements.

## License

Specify your license or state that the project is licensed under the MIT License.

## Contact

For any questions or suggestions, please contact [Christophe Le Dorze](mailto:christophe.ledorze@gmail.com).

