# Postmortem
## Issue Summary:
On 1/1/17 at 4:10 pm, a startup lanched their new feature on their wordpress platform and they did all the marketing and expected a larger increase in profit after users pay for this features, But after 3 min from lunching the website service was totaly down for 17 min. The root cause was a typographical error in wordpress-setting file in wich the word 'php' typed as 'phpp', This outrage affected a lot of users and the the buissness company itself.

## Timeline for 1/1/17 :
**4:13 pm:** An engineer noticed that the website was returning on a 500 status code.

**4:15 pm:** The running processes on the server were checked using `ps auxf`. He found an error with PHP/WordPress.

**5:17 pm:** The engineer was scanning  WordPress configuration file `/var/www/html/wp-config.php`.

**5:23 pm:** An typographical error found.

**5:24 pm:** The typographical error was fixed using `sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php`. 

**5:25 pm:** Website service was then tested one more time.

**5:30 pm:** Eveything deployed an works fine.

## Root cause && resolution:
The root cause was  a typographical error in the word '.php' in the wp-settings.php file. The error caused a 100% outage cause the error stoped all services and prevented content from being served. 

## preventative measures:
In order to prevent outages like this in the feature the comany should set up an isolated docker containers for testing purposes before deployment.
