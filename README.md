![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# The Zen of Typing

#### [Live link to deployed project](https://zen-of-typing.herokuapp.com/)

![in-game screenshot of deployment terminal](docs/images/screenshots/in-game-deployed.png)

[The Zen of Typing](https://zen-of-typing.herokuapp.com/) is a Python terminal project whose primary purpose is to enable users to practice and improve their touch typing skills.

Secondarily, it serves to reinforce various (mainly Python-related) programming principles and aphorisms through the use of carefully-selected practice texts and extracts.

Users can customise their experience by choosing from a range of options before the game itself gets underway. Once all necessary pre-game instructions have been displayed and the target text is loaded, the user's performance is monitored as they attempt to replicate each line of text. As soon as they finish and hit **Enter**, they receive feedback in the form of a breakdown of their typing speed and accuracy. They may then choose to either restart the game or quit (and exit the application).

## How to play

The Zen of Typing is loosely modelled on classic typing programmes such as ['Mavis Beacon Teaches Typing!'](https://en.wikipedia.org/wiki/Mavis_Beacon_Teaches_Typing), which the developer was known to spend countless hours practicing throughout his misspent youth.

The title is also a play on ['The Zen of Python'](https://www.python.org/dev/peps/pep-0020/), Pythoneer [Tim Peters'](https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer)) list of fundamental commandments for the then-nascent programming language, which was first issued in 1999 and has since come to be seen as something of a cornerstone document.

To begin, a welcome message is communicated on the start screen and the user is asked if they would like to warm up by tackling a practice text (which is subsequently revealed to be [Tom Cargill's humorous observation now known as the 'ninety-ninety rule'](https://en.wikipedia.org/wiki/Ninety%E2%80%93ninety_rule)).

Following this optional practice session - which they can take as many times as they wish - the user is given a multiple-choice menu of target texts, from which they must choose one by using the Up, Down and Enter keys on their keyboard. There are six texts in all, each of which is denoted by a slightly cryptic title/acronym. If the user finds that they are struggling to decide on a text, they may opt to effectively 'roll the dice' by asking the computer to pick one at random for them.

Once a text has been chosen, a subsequent menu similarly asks the listener to choose from a range of options, this time corresponding to the number of lines they wish to type. The list is once again navigated using the Up, Down and Enter keys.

Having selected both a text and the number of lines to be typed, the user is next asked if they know the secret password. This time they must provide an answer by inputting either 'Y' or 'N' on their keyboard.

- If they **don't** know it, a summary of their choices is displayed and the target text is outputted in italics. A bold yellow "Off you go!!!" message signals that the game is underway and they must begin the typing task.

- If, on the other hand, they **do** know the secret password (and indicate so by pressing 'Y'), they are prompted to enter it as an input string.
  - If the password they enter happens to be incorrect, they are alerted to this fact by a bold red feedback message, after which the password functionality is discarded and the game begins in the usual fashion (see above)
  - If they enter a correct password, meanwhile, they unlock a bonus submenu offering the chance to acticate the 'Beast Mode' feature (explained in more detail below).

## Features

### Existing features:

- #### Python-centric ASCII art hero image and colour scheme

  <details>
    <summary>
    <b>click to view</b>
    </summary>

  The prevalent blue and yellow design palette both draws the user's attention and reinforces the fact that this is very much a [Python](https://en.wikipedia.org/wiki/File:Python-logo-notext.svg) application. Elsewhere, semantic text feedback is displayed in a familiar and intuitive fashion, e.g. error messages in red, success alerts in green. While many terminal projects can look drab and monotone, it was the developer's intention that The Zen of Typing should be anything but.

</details>

- #### Immersive sequential flow of multiple-choice menus and questions (enabled c/o the [PyInquirer module](https://github.com/CITGuru/PyInquirer))

  <details>
    <summary>
    <b>click to view</b>
    </summary>

  From a UX standpoint, the [closed-ended](https://en.wikipedia.org/wiki/Closed-ended_question) nature of almost all of the questions with which the user is presented minimises the risk of error and all but eliminates the possibility of invalid user input. This saves time (for both developer and user), while also delivering a neat and concise pre-game interface.

</details>

- #### Warm-up/Practice option

  <details>
    <summary>
    <b>click to view</b>
    </summary>

  Not everyone is a super-fast expert typist. Similarly, not everyone produces their finest work under pressure. Bearing this in mind, The Zen of Typing allows users to practice their typing in a relaxed fashion without having to worry about performance metrics (the practice mode is not 'recorded', i.e. no speed/accuracy calculations are made). They may then progress to the stricter in-game conditions whenever they feel ready.

</details>

- #### Randomised text selection fallback option

  <details>
    <summary>
    <b>click to view</b>
    </summary>

  [Hick's Law](https://lawsofux.com/hicks-law/) states that "the time it takes to make a decision increases with the number and complexity of choices". If, therefore, the user feels somewhat overwhelmed at having to choose between the six available target texts, they can simply ask the [random module](https://docs.python.org/3/library/random.html) to help lighten their cognitive load by deciding for them.

</details>

- #### Programming-focused target text content

  <details>
    <summary>
    <b>click to view</b>
    </summary>

  Five of the six available target texts are directly related to computer programming, with a strong Python emphasis. While it would arguably have been simpler to work with generic/filler content, this way the Zen of Typing user stands to kill two birds with one stone (so to speak) by rounding out their coding knowledge as they're working on their typing speed.

</details>

- #### API integration

  <details>
    <summary>
    <b>click to view</b>
    </summary>

  One of the five programming-related target texts mentioned above is actually a dynamically-generated random list of responses from an end-point associated with the [pyjokes ("jokes as a service") API](https://pyjok.es/).

  ![pyjokes logo](docs/images/icons/logo-pyjokes.png)

</details>

- #### Gamification

  <details>
    <summary>
    <b>click to view</b>
    </summary>

  One surefire way to drive user engagement is to harness the principles of [operant conditioning](https://en.wikipedia.org/wiki/Operant_conditioning) when designing an interactive application. The Zen of Typing adheres to this objective on at least two fronts:
  - The user is provided with instant feedback in the form of a results breakdown, consisting of overall time taken, accuracy and average speed (in words typed per minute). In most cases, this alone should be enough of a hook to encourage them to keep playing in the hope of improving on their current 'personal best' score(s)
  - The secret password/'Beast Mode' functionality is initially alluded to in passing, but quickly becomes a central aspect of the game. Crucially, the user is never directly informed as to how and when the next character of this password will be revealed, so they are kept guessing (and wanting more) to a large extent.

</details>

- #### Input validation and error-checking

  <details>
    <summary>
    <b>click to view</b>
    </summary>

  The one open-ended question demanding user input is the secret password prompt. This is handled in a straightforward binary fashion: if the user enters anything other than the correct (case-sensitive) password, they are informed of their mistake and the game simply starts as normal. This is accomplished by using a compound if statement within the game class's main `activate()` method. 

</details>

### Potential future features:

<details>
  <summary>
  <b>click to view</b>
  </summary>

- #### Individual breakout pages for each country:

  Given more time, I would have been able to build this expanded feature into the current version of the app. A standalone component could be dynamically populated with more granular information about each country's medal haul: for example, appropriate use of React icons could highlight the Olympic events in which that particular nation was successful. Names of athletes/winners could also be listed, perhaps along with a more detailed look at that country's Olympic Games success rate historically.

- #### Aggregate the data to compile relative medal-winning stats for each of the five continents represented by the Olympic rings:

  This would be a fun and interesting add-on I feel, and would once again shine a slightly alternative light on what is a veritable ocean of Olympics-related stats and datasets. It would actually be quite easy to implement, and could similarly be used to run down both total and per capita figures for each continent.

- #### Expand the scope of the project to also incorporate the Tokyo 2020 Paralympic Games:

  More than just a nice-to-have, this is a feature that ought really to have been included from the start in the current MVP. However, three factors combined to prevent me from readily including corresponding figures for Paralympic medal-winning countries:

  - There simply isn't the same availability of data (and/or APIs) related to the Paralympics, so a good bit more digging would have been required to find appropriately malleable numbers
  - The Paralympic Games were still actually taking place throughout most of this project's development life cycle, and so trying to gather data would necessarily have constituted something of a 'moving target' exercise
  - Finally, as is so often the case, the project deadline approached quicker than I would have liked, and I was mindful of [not falling into the familiar trap](https://quotefancy.com/quote/757101/Tom-Cargill-The-first-90-percent-of-the-code-accounts-for-the-first-90-percent-of-the) of feature creep

- #### ["Infinite scroll"](https://www.npmjs.com/package/react-infinite-scroll-component) and/or pagination:

  One of a number of necessary trade-offs made to ensure the overall project made it over the finish line inside its submission dealine. A dynamic 'back-to-top' button component has been put in place to compensate for the absence of both of the above, and it is hoped this will help improve UX sufficiently until such time as I'm able to add these convenient features.

- #### Site-wide dark mode:

  At present, the user is only able to toggle dark mode on or off while browsing the main Medallists page. Ideally, this feature should be available throughout the application to give a more coherent and complete feel. However, it's worth noting that the site's [About page](https://going-for-gold.netlify.app/about) has been styled with a 'dark mode-like' background colour by default, and that the neumorphic styling that's been applied to the [Contact form](https://going-for-gold.netlify.app/contact) would also likely be affected by dark mode being enabled there.
  </details>

## Technologies Used

### Languages:

<details>
  <summary>
    <b>click to view</b>
  </summary>

- [HTML5:](https://en.wikipedia.org/wiki/HTML5) used for structuring the site
- [CSS3:](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) used for styling the site
- [JavaScript:](https://en.wikipedia.org/wiki/JavaScript) used for site logic and web page behaviour
- [JSX](<https://en.wikipedia.org/wiki/JSX_(JavaScript)>) used to structure React component rendering throughout the application
</details>

### Frameworks/Libraries, APIs, , Projects, Programmes and Tools:

<details>
  <summary>
    <b>click to view</b>
  </summary>

- ES6 imports:

  - [React v16.13.1:](https://reactjs.org/) used as a base to create dynamic user interfaces by building and customising modular components, as well as handling state management and rendering that state to the DOM
  - [ReactDOM v16.13.1:](https://reactjs.org/docs/react-dom.html) used to give the app access to various top-level DOM-specific methods
  - [React Icons v4.2.0:](https://react-icons.github.io/react-icons/) used to include individual bespoke icons where needed within the project
  - [react-resize-detector v6.7.6:](https://www.npmjs.com/package/react-resize-detector) used to leverage native browser resize handling to manage element resize events within the app's components
  - [React Router v5.2.0:](https://reactrouter.com/) used to provide declarative routing for the application
  - [Create React App v3.4.3:](https://create-react-app.dev/) used to get application development off the ground by overseeing configuration of build tools, bundle optimisation, directory structure etc.
  - [Google Fonts:](https://fonts.google.com/) used to import the Raleway font into the project's stylesheet
  - [Visual Studio Code:](https://code.visualstudio.com/) used as the online IDE for the project
  - [Git:](https://git-scm.com/) used for version control by utilising the Gitpod terminal to commit frequently to Git and push all commits to GitHub
  - [GitHub:](https://github.com/) used to compile and remotely store the project's codebase following successive local commits initiated from the command line
  - [Netlify:](https://www.netlify.com/) used to deploy the site and aid workflow in line with serverless continuous deployment best practices
  - [Fetch API:](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) used to make API requests and retrieve resources and/or responses returned by them
  - [(React) Context API:](https://reactjs.org/docs/context.html) used to pass data through the app's component tree without having to pass props down manually at every level
  - [REST Countries API:](https://restcountries.eu/) used to collect population data and flag images corresponding to each of the 93 countries featured in the list(s) of Olympic medal-winners
  - [EmailJS v3.2.0:](https://t.co/L61tIINT0d?amp=1) used to route messages submitted via the site's [Contact form](https://going-for-gold.netlify.app/contact) to the site owner/developer's email address
  - [GSAP (GreenSock Animation Platform) v3.7.1:](https://greensock.com/gsap/) imported and used to implement the site's marquee [landing page animation](https://going-for-gold.netlify.app/contact)
  - [Ezgif image converter:](https://ezgif.com/webp-to-jpg) used to convert several of the project image source files from `.svg` to `png/jp(e)g` formats
  - [Neumorphism.io:](Neumorphism.io) Open-source 'Soft UI' CSS shadow generator used when styling the site's [Contact form](https://going-for-gold.netlify.app/contact)
  - [ColorSpace's online colour gradient generator](https://mycolor.space/gradient) was used to apply a metallic shine effect to the gold-, silver- and bronze-coloured landing page buttons, and to create the linear gradients found elsewhere
  - [Box Shadow CSS Generator:](https://cssgenerator.org/box-shadow-css-generator.html) Used to add subtle shadow styling to most clickable elements across the site
  - The project's favicon was generated using the [free online favicon.io tool](https://favicon.io/favicon-converter/)
  - The [JPG to PNG online editing tool](https://jpg2png.com/) was used to convert a `.jpeg` version of the Tokyo 2020 logo to `.png` format
  - [TinyJPG:](https://tinyjpg.com/) used for image compression
  - [PicResize:](https://picresize.com/) used to crop and resize images
  - [Brackets](http://brackets.io/) (desktop app version): used to make colouration edits to SVG files
  - [Kapwing:](https://www.kapwing.com/) used as the project's go-to content editing resource, e.g. to create the [animated](#going-for-gold) [screenshots](#about-page) featured in this README
  - [W3Schools HTML Color Picker:](https://www.w3schools.com/colors/colors_picker.asp) used for generating on-the-fly colour pairings and modifications (lightening, darkening etc. of core project colours)
  - [Responsively App:](https://responsively.app/) Used to frequently test and inspect responsive layout and component rendering as the project took shape
  - [WebAIM (contrast checker):](https://webaim.org/resources/contrastchecker/) / [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) used to ensure site foreground and background colour contrasts meet [WCAG 2 accessibility requirements](https://webaim.org/articles/contrast/)
  - [Can I Use:](https://caniuse.com/) browser compatibility tables used to cross-reference the viability of implementing certain HTML5 elements, CSS3 properties, file formats and more
  - [Editor.md:](https://pandao.github.io/editor.md/en.html) used to format project Markdown in line with best practices

</details>

## Data Model

<details>
  <summary>
    <b>click to view</b>
  </summary>

### Netlify:

This project has been deployed to [Netlify](https://www.netlify.com/) using continuous deployment in sync with [GitHub](https://en.wikipedia.org/wiki/GitHub). A full step-by-step guide to what's involved in setting up this workflow can be found [here](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/)

### Forking the GitHub Repository:

It is possible to fork this GitHub repository to view and/or make changes without affecting the original. This is achieved by following these steps...

1. [**Sign in** to your GitHub account](https://github.com/login) and locate the [relevant repository](https://github.com/loosenthedark/going-for-gold).
2. Click on **Fork**, located near the top right-hand corner of the repository page.
3. You will now have a copy of this project's repository in your own GitHub account.

### Making a local clone:

It is possible to copy the repository to your local machine so that you can fix merge conflicts, add or remove files and push larger commits without affecting the original project code. Cloning a repository pulls down a full copy of all the repo data that GitHub has at that point in time. See the [GitHub Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) for further information, and below for a brief summary...

1. [**Sign in** to your GitHub account](https://github.com/login) and locate the [relevant repository](https://github.com/loosenthedark/going-for-gold).
2. Click on the **Code** dropdown next to the green **Gitpod** button. This will reveal the **Clone** option.
3. In order to clone the repository using `HTTPS`, select **HTTPS** and copy the link shown (there is a copy button to the right of the URL).
4. Next, open **Git Bash** (see [here](https://git-scm.com/downloads) for an overview of download options, if required).
5. Change the current working directory on your local machine to the location where you want the cloning to be made.
6. Type `git clone` into your IDE terminal followed by the URL you copied in Step 3 above, i.e.

```
https://github.com/loosenthedark/going-for-gold.git
```

7. Press **Enter**.
8. Your local clone has now been created.

_See the [GitHub Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories) for more information on all of the above processes._

</details>

## Testing

<details>
  <summary>
    <b>click to view</b>
  </summary>

### Bugs:

This project has been deployed to [Netlify](https://www.netlify.com/) using continuous deployment in sync with [GitHub](https://en.wikipedia.org/wiki/GitHub). A full step-by-step guide to what's involved in setting up this workflow can be found [here](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/)

#### Solved Bugs:

It is possible to copy the repository to your local machine so that you can fix merge conflicts, add or remove files and push larger commits without affecting the original project code. Cloning a repository pulls down a full copy of all the repo data that GitHub has at that point in time. See the [GitHub Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) for further information, and below for a brief summary...

#### Remaining Bugs:

It is possible to copy the repository to your local machine so that you can fix merge conflicts, add or remove files and push larger commits without affecting the original project code. Cloning a repository pulls down a full copy of all the repo data that GitHub has at that point in time. See the [GitHub Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) for further information, and below for a brief summary...

### Validation:

This project has been deployed to [Netlify](https://www.netlify.com/) using continuous deployment in sync with [GitHub](https://en.wikipedia.org/wiki/GitHub). A full step-by-step guide to what's involved in setting up this workflow can be found [here](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/)

</details>

## Deployment

### GitHub

<details>
  <summary>
    <b>click to view</b>
  </summary>

This project was developed in a repository built on top of the [Code Institute Python Essentials template repository](https://github.com/Code-Institute-Org/python-essentials-template), thus inheriting the latter's main directory structure and starter files.

Creating the repository from the template involved following each of these steps:

1. On GitHub.com, navigate to the main page of the template repository - in this case, [this page](https://github.com/Code-Institute-Org/python-essentials-template).

2. Above the file list, click **Use this template**.

3. On the next screen, select the account you want to own the repository from the **Owner** drop-down menu.

4. Enter a **Repository name**, as well as an optional **Description**.

5. Choose a repository visibility. NB: To meet Code Institute project submission criteria, this must be set to **Public**.

6. Click **Create repository from template**.
</details>

### Forking the GitHub Repository

<details>
  <summary>
    <b>click to view</b>
  </summary>

It is possible to fork this project's GitHub repository to view and/or make changes without affecting the original. This is achieved by following these steps...

_NB: The steps outlined below assume that you already have [Git](https://git-scm.com/) set up on your computer - for an overview of how to download, install, and configure Git, consult the [GitHub Docs](https://docs.github.com/en/github-ae@latest/articles/set-up-git)_

1. [**Sign in** to your GitHub account](https://github.com/login) and locate the [relevant repository](https://github.com/loosenthedark/zen-of-typing).
2. Click on **Fork**, located near the top right-hand corner of the repository page.
3. You will now have a copy of this project's repository in your own GitHub account.
</details>

### Making a local clone

<details>
  <summary>
    <b>click to view</b>
  </summary>

It is possible to copy the repository to your local machine so that you can fix merge conflicts, add or remove files and push larger commits without affecting the original project code. Cloning a repository pulls down a full copy of all the repo data that GitHub has at that point in time. See the [GitHub Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) for further information, and below for a brief summary...

1. [**Sign in** to your GitHub account](https://github.com/login) and locate the [relevant repository](https://github.com/loosenthedark/zen-of-typing).
2. Click on the **Code** dropdown next to the green **Gitpod** button. This will reveal the **Clone** option.
3. In order to clone the repository using `HTTPS`, select **HTTPS** and copy the link shown (there is a copy button to the right of the URL).
4. Next, open **Git Bash** (see [here](https://git-scm.com/downloads) for an overview of download options, if required).
5. Change the current working directory on your local machine to the location where you want the cloning to be made.
6. Type `git clone` into your IDE terminal followed by the URL you copied in Step 3 above, i.e.

```
https://github.com/loosenthedark/zen-of-typing.git
```

7. Press **Enter**.
8. Your local clone has now been created.

_See the [GitHub Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories) for more information on all of the above processes._
</details>

### Heroku

<details>
  <summary>
    <b>click to view</b>
  </summary>

The application is deployed on [**Heroku**](https://heroku.com/), and can be accessed using the following URL: https://zen-of-typing.herokuapp.com/

The steps involved in deploying to Heroku were as follows:

1. Create a `requirements.txt` file from the command line, and populate it with a list of project dependencies:

  ```
  pip3 freeze > requirements.txt
  ```

2. Save, commit and push your changes to GitHub.

3. Create a `Procfile`

  ```
  echo web: node index.js > Procfile
  ```

_NB: This file comes baked-in with the [Code Institute project template repository](https://github.com/Code-Institute-Org/python-essentials-template), so can be skipped if you are using that in your own build_

4. Create an account with Heroku, selecting Python as the primary development language.

5. [Log in to your account](https://id.heroku.com/login), and in the top right-hand corner of the **Dashboard** click on **New > Create new app**

6. Enter a unique name for your app and select your region. Click on **Create app**.

7. Go to **Settings**

8. Click on the **Reveal Config Vars** button in the 'Config Vars' section.

9. Enter PORT in the KEY field and 8000 in the VALUE field.

10. In the 'Buildpacks' section further down the settings page, click on **Add buildpack**.

11. Select **python** and **nodejs** from the menu of "officially supported buildpacks". 

_NB: Python must be placed at the top of your app's buildpack list. You can drag and drop your buildpacks to reposition them if necessary._

12. Go to **Deploy**.

13. Select **GitHub** in the 'Deployment method' section.

14. In the 'Connect to GitHub' section, search for the repository you wish to use, then click **Connect**.

15. Ensure that the project's main or master branch (depending on which is being used as the primary branch) is selected under 'Deploy a GitHub branch' in the 'Manual deploy' section.

_NB: If you choose to **Enable Automatic Deploys**, Heroku will rebuild the app every time you push a change to GitHub (which is considered best practice in most instances)._

15. After clicking on the **Deploy Branch** button, you should see a message confirming that "Your app was successfully deployed" followed by a **View** button which can be clicked to launch and view the app.
</details>

## Credits

### Code:

Where code blocks/snippets/suggestions have been incorporated from external sources into this project's code, these have been noted through the use of comments. Beyond this, the developer made use of the following articles, workarounds and learning resources while building the site:
<details>
  <summary>
    <b>click to view</b>
  </summary>

- ['Bootstrap 4 simple back to top with smooth scroll'](https://bbbootstrap.com/snippets/simple-back-top-smooth-scroll-17111555) (BBBootstrap)
- ['Show div after 500px scroll'](https://jsfiddle.net/amirsaleem/xpd1wr7n/) (JSFiddle)
- ['How to crop SVG file within HTML/CSS'](https://stackoverflow.com/questions/37588405/how-to-crop-svg-file-within-html-css/37589395) (Stack Overflow)
- ['CSS Clipping Path with CSS Shapes'](https://codepen.io/heyitsolivia/pen/EICDK?editors=1100) (CodePen)
- ['A Complete Guide to Grid'](https://css-tricks.com/snippets/css/complete-guide-grid/) (CSS-Tricks)
- ['15 Compelling Above the Fold Content Examples to Inspire Your Own'](https://blog.hubspot.com/marketing/above-the-fold) (HubSpot)
- ['Create a Website With Video Background'](https://www.youtube.com/watch?v=8MgpE2DTTKA) (Traversy Media)
- ['How do I loop through multiple background videos?'](https://stackoverflow.com/questions/54380721/how-do-i-loop-through-multiple-background-videos) (Stack Overflow)
- ['How to detect Safari, Chrome, IE, Firefox and Opera browser?'](https://stackoverflow.com/questions/9847580/how-to-detect-safari-chrome-ie-firefox-and-opera-browser) (Stack Overflow)
- ['How to change the playing speed of videos in HTML5?'](https://stackoverflow.com/questions/3027707/how-to-change-the-playing-speed-of-videos-in-html5)] (Stack Overflow)
- [’How can one display images side by side in a GitHub README.md?](https://stackoverflow.com/questions/24319505/how-can-one-display-images-side-by-side-in-a-github-readme-md) (Stack Overflow)
- ['`<details>`: The Details disclosure element'](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) (MDN Web Docs)
  - My mentor kindly alerted me to this means of making my README more compact and readable via [his own demo implementation](docs/images/screenshots/details.png)
- [Morten Rand-Hendriksen](https://twitter.com/mor10)'s [LinkedIn Learning courses](https://www.linkedin.com/learning/instructors/morten-rand-hendriksen) on CSS, and in particular his advice on the principles of [progressive enhancement](docs/images/screenshots/mor10-progressive-enhancement.png) proved especially useful when implementing a CSS grid layout for larger screens
</details>

### Content:
<details>
  <summary>
    <b>click to view</b>
  </summary>

- Most of the `body` text was composed by the developer, and is an extension of the content on Brew Barberista's existing site, along with relevant supplementary information found across the business's social media channels
- The [social proof copy (customer reviews)](https://loosenthedark.tech/brew-barberista/#customer-reviews) is all legitimate and authentic - below are links to the originals of each featured quote:
  - [Tripadvisor review](https://www.tripadvisor.ie/ShowUserReviews-g186605-d23032935-r780386055-Brew_Barberista-Dublin_County_Dublin.html#REVIEWS)
  - [Lovin Dublin quote](https://lovindublin.com/amp/food-drink/22-of-dublins-best-sausage-rolls-as-voted-by-you?utm_campaign=article&utm_source=twitter&utm_medium=web)
  - [Google Review #1](https://www.google.com/maps/contrib/103803718842789538353/reviews/@53.3810542,-6.1654387,17z/data=!3m1!4b1!4m3!8m2!3m1!1e1?hl=en-IE)
  - [Google Review #2](https://goo.gl/maps/sTyXPyPDziQCF67W9)
</details>

### Media:
<details>
  <summary>
    <b>click to view</b>
  </summary>

| [**Website section**] Media title/description  | Media format  | Credit  | Link to original media source(s)  | 
| :------------ |:--------------- |:-----|:---------------|
| **`head`**         |                 |      |                |
| Brew Barberista circular brand logo      | image        | [Brew Barberista](http://brewbarberista.ie/)      | [Brew Barberista website header](http://brewbarberista.ie/resources/Circular%20logo.jpg)      |
| Brew Barberista owner press pic      | photo        | [Frank McGrath](https://www.facebook.com/FrankMcgrathPhotography)      | [Independent.ie](https://www.independent.ie/irish-news/a-cut-above-the-new-barber-offering-a-proper-coffee-while-you-get-your-hair-cut-39820368.html)      |
| **`nav`**         |                 |      |                |
| Brew Barberista main brand logo      | image        | [Brew Barberista](http://brewbarberista.ie/)      | [Brew Barberista website header](http://brewbarberista.ie/resources/Circular%20logo.jpg)      |
| gold hamburger icon      | icon        | [Font Awesome](https://fontawesome.com/license)      | [Font Awesome](https://fontawesome.com/v5.15/icons/bars?style=solid)      |
| gold coffee mug icon      | icon        | [Font Awesome](https://fontawesome.com/license)      | [Font Awesome](https://fontawesome.com/v5.15/icons/mug-hot?style=solid)      |
| **`header`**         |                 |      |                |
| 'Calm Sea Under Blue Sky'      | photo  | [cottonbro](https://www.pexels.com/@cottonbro)      | [Pexels](https://www.pexels.com/photo/calm-sea-under-blue-sky-4571251)      |
| 'Fashion silhouette hipster style'      | vector illustration  | [RomanYa](https://www.shutterstock.com/g/RomanYa)      | [Shutterstock](https://www.shutterstock.com/image-vector/fashion-silhouette-hipster-style-vector-illustration-161463794)      |
| 'Paper mug with hot drink inside'      | vector illustration  | [Agnieszka Karpinska](https://www.shutterstock.com/g/Panptys)      | [Shutterstock](https://www.shutterstock.com/image-vector/paper-mug-hot-drink-inside-vector-322930262)      |
| 'A Barista Making A Coffee Artistically'      | video  | [Ketut Subiyanto](https://www.pexels.com/@ketut-subiyanto)      | [Pexels](https://www.pexels.com/video/a-barista-making-a-coffee-artistically-4378109/)      |
| 'A Man Shaving A Man's Facial Hair'      | video  | [Pavel Danilyuk](https://www.pexels.com/@pavel-danilyuk)      | [Pexels](https://www.pexels.com/video/a-man-shaving-a-man-s-facial-hair-4178140/)      |
| **`main`**         |                 |      |                |
| 'Cold Brew'      | photo      | [Andrew "Donovan" Valdivia](https://unsplash.com/@donovan_valdivia?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)      | [Unsplash](https://unsplash.com/photos/mMI5sdLFoHMt)      |
| 'Anonymous barista pouring milk from jug into paper cup'      | photo  | [Ketut Subiyanto](https://www.pexels.com/@ketut-subiyanto)      | [Pexels](https://www.pexels.com/photo/anonymous-barista-pouring-milk-from-jug-into-paper-cup-4350051/)      |
| barber's kit against orange background      | photo      | [Sinval Carvalho](https://unsplash.com/@sinvalbmx)      | [Unsplash](https://unsplash.com/photos/WbEibGKHBMY)      |
| 'Baked Pastries'      | photo      | [Magda Ehlers](https://www.pexels.com/@magda-ehlers-pexels)      | [Pexels](https://www.pexels.com/photo/baked-pastries-2573870)      |
| 'Brown Coffee Beans on Gray Textile'      | photo      | [Liana Horodetska](https://www.pexels.com/@liana-horodetska-5077625)      | [Pexels](https://www.pexels.com/photo/dawn-caffeine-coffee-dark-7507365/)      |
| 'Man in White and Black Stripe Shirt Holding Black Pen'      | photo      | [cottonbro](https://www.pexels.com/@cottonbro)      | [Pexels](https://www.pexels.com/photo/man-in-white-and-black-stripe-shirt-holding-black-pen-3998429/)      |
| 'White Ceramic Mug With Brown Liquid'      | photo      | [Gareth Rees](https://www.pexels.com/@gareth-rees-2793957)      | [Pexels](https://www.pexels.com/photo/white-ceramic-mug-with-brown-liquid-4334758/)      |
| 'Straight Razor Kit'      | photo      | [Josh Sorenson](https://www.pexels.com/@joshsorenson)      | [Pexels](https://www.pexels.com/photo/straight-razor-kit-995300/)      |
| 'Set of disposable paper coffee cups'      | photo      | [Ketut Subiyanto](https://www.pexels.com/@ketut-subiyanto)      | [Pexels](https://www.pexels.com/photo/set-of-disposable-paper-coffee-cups-4349942/)      |
| customer avatars      | photos        | [UI Faces](https://uifaces.co/license) / [Random User Generator](https://randomuser.me/copyright)      | [#1](https://randomuser.me/api/portraits/women/26.jpg) / [#2](https://uifaces.co/our-content/donated/l1qF9oeF.jpg) / [#3](https://randomuser.me/api/portraits/men/43.jpg)      |
| Lovin Dublin avatar      | image        | [Lovin Dublin](https://t.co/Qz2mocJaYK?amp=1)      | [Lovin Dublin Twitter profile](https://twitter.com/LovinDublin/photo)      |
| Brew Barber customer black & white image     | photo        | [Brew Barberista Facebook page](https://www.facebook.com/brew.barberista)      | [Facebook](https://www.facebook.com/photo.php?fbid=246151787283327&set=pb.100056655232619.-2207520000..&type=3)      |
| 3fe logo      | logo        | [3fe](https://3fe.com/)      | [3fe website](https://3fe.com/uploads/3fe-social.jpg)      |
| Victoria Arduino logo      | logo        | [Victoria Arduino](https://www.victoriaarduino.com/)      | [Jimmy's Espresso Services](https://www.jimmys-espresso.co.uk/wp-content/uploads/2019/02/victoria-arduino-Narrow-Logo1-400.jpg)      |
| Tartine Organic Bakery logo      | logo        | [Tartine](https://www.tartine.ie/)      | [Veganic](https://veganic.ie/wp-content/uploads/2020/08/Tartine-Logo.jpg)      |
| Pieman logo      | logo        | [Pieman](https://www.thepieman.ie/)      | [Pieman website](https://images.squarespace-cdn.com/content/v1/58ab0e006b8f5bc50827b39e/1490268707882-D78IF5OH3SWO1502QB35/image-asset.png)      |
| Nic Gemma Cupcakes logo      | logo        | [Nic Gemma Cupcakes](https://www.instagram.com/nicgemmacupcakes/)      | [Nic Gemma Instagram page](https://scontent-dub4-1.cdninstagram.com/v/t51.2885-19/s320x320/145182603_3018544658415446_2135604228419315042_n.jpg?_nc_ht=scontent-dub4-1.cdninstagram.com&_nc_ohc=i2UDd_VT8ggAX9kCAwN&edm=ABfd0MgBAAAA&ccb=7-4&oh=a3bd6c9fd36b16adf253dc9f2c1d2e4a&oe=610BCD9E&_nc_sid=7bff83)      |
| The Raw Juice Company logo      | logo        | [The Raw Juice Company](https://raw.ie/)      | The Raw Juice Company [website](https://raw.ie/img/raw-food-and-beverage-solutions-logo-1605189335.jpg) & [Facebook page](https://www.facebook.com/The-Raw-Juice-Company-Ireland-113344153656389/photos/a.113344320323039/113489553641849)      |
| Korina Bakery logo      | logo        | [Korina Bakery](https://www.thegreendoor.ie/korina-bakery)      | [Korina Bakery Facebook page](https://www.facebook.com/korinabakery/photos/a.2251060755165684/2251062425165517)      |
| Tonja Maguire Art logo      | logo        | [Tonja Maguire Art](https://www.tonjamaguireart.com/)      | [Tonja Maguire Art Facebook page](https://www.facebook.com/Tonjamaguireart/photos/a.401354727329500/402379617227011)      |
| Conscious Cup Campaign logo      | logo        | [Conscious Cup Campaign](https://www.consciouscup.ie/)      | [Conscious Cup Campaign website](https://www.consciouscup.ie/images/cropped-cc_wp_headerb4.png)      |
| Pieta Darkness Into Light logo      | logo        | [Pieta](https://www.pieta.ie/)      | [Darkness Into Light 2021 website](https://www.darknessintolight.ie/home-page-2021)      |
| St. Francis Hospice logo      | logo        | [Saint Francis Hospice](https://www.sfh.ie/)      | [Laimoon](https://cdn.laimoon.com/content_1431673462-kp10.jpg)      |
| Raheny Business Association logo      | logo        | [Raheny Business Association](https://www.rahenybusiness.com/)      | [Raheny Business Association website](https://images.squarespace-cdn.com/content/v1/5a79bf21f9a61eae5ef4b493/1518545668706-0DFZ2XTG3NMNYHHRYJAW/Raheny-Business-Association-Logo-Revised.png?format=1500w)      |
| **`footer`**         |                 |      |                |
| 'Gmail New 2020 Vector'      | vector icon  | [IconApe](https://iconape.com/)      | [IconApe](https://iconape.com/gmail-new-2020-seeklogo-com-3-logo-icon-svg-png.html)      |
| 'Dog Friendly sign'      | image  | [SVGCraftLounge](https://www.etsy.com/ie/shop/SVGCraftLounge?ref=l2-about-shopname)      | [Etsy](https://www.etsy.com/ie/listing/1046348333/dog-friendly-sign-printable-and-cut-file?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=no+pets+allowed+png&ref=sr_gallery-2-26&pro=1)      |
</details>

### Acknowledgments:

- I've been fortunate enough to be paired with an incredibly helpful and approachable mentor in [Tim Nelson](https://github.com/TravelTimN). He has been on hand throughout this project's evolution to offer pointers, timely feedback and guidance. Cheers, Tim!
- My better half Ana deserves a medal, not just a mention, for all her constant support and encouragement. She also conducted plenty of ad hoc testing on a range of devices, and it was she who suggested I speed up the background barista video above the fold on desktop 😁

![Brew Barberista responsive footer device mockups](docs/images/screenshots/mockups/brew-barberista-footer.png)

## Notice

This site has been created for development purposes only.

![Python logo wallpaper background](docs/images/bg-python.png)

['PEP 20 -- The Zen of Python'](https://www.python.org/dev/peps/pep-0020/) (Python.org)

['Don't repeat yourself'](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Wikipedia)

['Object-oriented programming'](https://en.wikipedia.org/wiki/Object-oriented_programming) (Wikipedia)

['From virtualenv, pip freeze > requirements.txt give TONNES of garbage! How to trim it out?'](https://stackoverflow.com/a/41707616/12176426)

['12 Beginner Python Projects - Coding Course'](https://www.youtube.com/watch?v=8ext9G7xspg) (Kylie Ying/freeCodeCamp)

['History of Python' > 'Version 3'](https://en.wikipedia.org/wiki/History_of_Python#Version_3) (Wikipedia)

['Using global variables in a function'](https://stackoverflow.com/questions/423379/using-global-variables-in-a-function) (Stack Overflow)

[Python icon ASCII art](images/ascii-art.txt) copied from [this GitHub repo](https://github.com/honno/ascii-art) (though the original image source was [this subreddit](https://www.reddit.com/r/Python/comments/ifag14/python_logo_in_colored_ascii_art/))

The text content of the project's `sunscreen.txt` file is an abridged version of the lyrics to [Baz Luhrmann's 1997 spoken-word single 'Everybody’s Free (To Wear Sunscreen)'](https://genius.com/Baz-luhrmann-everybodys-free-to-wear-sunscreen-lyrics) (Genius)

['PEP 257 -- Docstring Conventions'](https://www.python.org/dev/peps/pep-0257/) (Python.org)

['How to let the user select an input from a finite list?'](https://stackoverflow.com/questions/37565793/how-to-let-the-user-select-an-input-from-a-finite-list#comment100075818_37567304) (Stack Overflow)

['How to Do Ternary Operator Assignment in Python'](https://www.webucator.com/article/how-to-do-ternary-operator-assignment-in-python/) (Webucator)

Valentin Bryukhanov's [PEP8 online checker](http://pep8online.com/) was used to validate the project's Python code, in line with best practice.

['How to split up a long f-string in python?'](https://stackoverflow.com/questions/48881196/how-to-split-up-a-long-f-string-in-python) (Stack Overflow)

['Creating a repository from a template'](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) (GitHub Docs)

['Ternary Operator in Python'](https://www.geeksforgeeks.org/ternary-operator-in-python/) (GeeksforGeeks)

['How to measure elapsed time in Python?'](https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python/7370824#7370824) (Stack Overflow)

[PyInquirer: "A Python module for common interactive command line user interfaces"](https://github.com/CITGuru/PyInquirer) (GitHub)

[pyjokes logo](https://pyjok.es/) (pyjokes Docs)

Python background wallpaper [sourced from Reddit](https://www.reddit.com/r/Python/)

Python logo used to create favicon [sourced from Wikipedia](https://en.wikipedia.org/wiki/File:Python-logo-notext.svg)

['pep8 warning on regex string in Python, Eclipse'](https://stackoverflow.com/a/19030982/12176426)

pyjokes: "One line jokes for programmers (jokes as a service)" - [GitHub](https://github.com/pyjokes/pyjokes) | [Docs](https://pyjok.es/install/)

['textwrap — Text wrapping and filling'](https://docs.python.org/3/library/textwrap.html) (Python Docs)

['How to print colored text to the terminal'](https://stackoverflow.com/a/39452138/12176426) (Stack Overflow)

['ANSI escape code'](https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters) (Wikipedia)

['Convert Images to ASCII Art'](https://manytools.org/hacker-tools/convert-images-to-ascii-art) (manytools.org)

['Ninety-ninety rule'](https://en.wikipedia.org/wiki/Ninety%E2%80%93ninety_rule) (Wikipedia)

['Create Your Own Python Projects'](https://www.linkedin.com/learning/python-projects-14276284/create-your-own-python-projects) (LinkedIn Learning)

### Bugs (+/- Bug Fixes):

![Bug: ValueError showing in deployment terminal](docs/images/screenshots/bugs/bug-valueerror.png)

Blinking ANSI code?

Prevent pasted-in text from validating

### Potential Future Features:

- ask user to enter email and send them a breakdown of their typing speed/accuracy (via smtplib module)?

- real-time user feedback, e.g. incorrectly-typed text highlighted in red so that the user can go back and correct mistake(s) (cf. [this example](https://mithil467.github.io/mitype/))

- Add padding to terminal output (chiefly the target text and/or user input) to improve readability and overall appearance (cf. [this blog post](https://stackabuse.com/padding-strings-in-python/))

- Bind secret password reveal functionality not just to typing speed, but also to accuracy
