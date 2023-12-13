# Email-Validity-Checker
This repository contains a Python Mini Project about Email Validity Checker using only Python built in functions &amp; methods

<hr>

## Valid Conditions If:
- Has the Name Format User@Hosting.Extension
- Usernames can only contain letters, numbers, underscores (_) and periods (.)
- Usernames can only start with letters or numbers
- Hosting names can only be letters or a combination of letters and numbers
- Extension names can only be letters and a maximum of 5 characters
- Special Character Symbols are not acceptable
- The number of @ can only be 1
- Example: .co.id or .co.sg will be considered 2 extensions, so each must follow the extension rules
- Maximum dot(.) for extension is only 2

<hr>

## Notification Example

Output example if the email is valid:

    Output Notification: The email address you entered is valid

If it is invalid, a notification will appear according to the reason:

    Output Notification:
    - Wrong Email Format (For example, No @, or no .extension)
    - The username format you entered is incorrect
    - The hosting format you entered is wrong
    - The extension format you entered is wrong

<hr>

## Email Example
Example of a Valid Email:

    - andre@gmail.com
    - joni_99@yahoo.com
    - andy.134@city.com
    - steve_roger.77@avengers01.space

Example of Invalid Email:

    - andre345@gmail
    - andre%$^@gmail.com
    - john@yah%%oo.com
    - tony_stark@stark.corporation
    - Thor@@gmail.com
