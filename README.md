# Instagram Converter
This script is to convert the .html files provided in a personal data export from Instagram into a .csv file for easy analysis.

## Usage
Run the script, ensuring that the HTML file you wish to convert is in the same directory as the script. When prompted, type the filename you wish to convert (e.g. messages.html) and run the code. The .csv file will have the same filename as the input HTML and will be in the same directory.

The message timestamp is in Pacific Standard Time (PST).

## Output
The outputted .csv file will be formatted as follows:


| Datetime  | From | Text | Attachments | Liked By |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 2023-11-30 17:36:00 | Username2  | Hey!  | messages/inbox/user_123456789/photos/123456789_123456789_01234567890123456789_n_12654782.jpg, messages/inbox/user_123456789/photos/123456789_01234567890123456_012345678901234_n_01234567890.jpg ||
| 2023-11-29 15:53:00  | Username1  | Hi!  || ❤️Username2  |

## To Do
 - Add support for group chats
 - Add audio and video attachment support

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
