# Changes

- File names not re-assigned correctly

       Changed the extention from .redacted.txt to .redacted

- Output files not stored in respective folder

      Changed the output function- used makedirs instead of mkdir


- Missing/No Features Found- Names

- Missing/No Features Found - Gender

- Missing/No Features Found- Phone Number

- Missing/No Features  Found- Concept

- Missing/No Features Found - Dates

- Missing/No Features - Addresses

- Missing Stats

       The reason for the above errors was because the file wasn't created

# Execution
``pipenv run python redactor.py --input "docs/*.txt" --names --dates --phones --genders --addresses --concept 'schedule' --concept 'gender' --stats stderr --output "outfiles/output"``

or

`pipenv run python redactor.py --input "tmp/*.txt" --names --dates --phones --genders --addresses --concept 'schedule' --concept 'gender' --stats stderr --output "outfiles/output"`

