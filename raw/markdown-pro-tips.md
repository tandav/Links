# Markdown Pro Tips
---
### Markdown table align
(use semicolons)
```md
| Left align | Right align | Center align |
|:-----------|------------:|:------------:|
| This       |        This |     This     |
| column     |      column |    column    |
| will       |        will |     will     |
| be         |          be |      be      |
| left       |       right |    center    |
| aligned    |     aligned |   aligned    |
```

---

* big

* line

* spaces

and

* small
* line
* spaces

---

`<kbd>SHIFT</kbd>` gives <kbd>SHIFT</kbd>

`<kbd>abcd... something</kbd>` gives <kbd>abcd... something</kbd>

maybe "⌘, ⇧, ⌥, ⌃, ⇪, Fn" looks better

---

### Markdown: Resize Images
* [image resize in github flavored markdown.](https://gist.github.com/uupaa/f77d2bcf4dc7a294d109)
* [Resize image in the wiki of GitHub using Markdown - Stack Overflow](http://stackoverflow.com/questions/24383700/resize-image-in-the-wiki-of-github-using-markdown)
* [image height + width attributes in markdown_github output · Issue #2554 · jgm/pandoc](https://github.com/jgm/pandoc/issues/2554)
* [Unable to control the size of images · Issue #164 · benweet/stackedit](https://github.com/benweet/stackedit/issues/164)
* [Controlling image size in a simple way in Markdown · Issue #4 · jeromyanglim/rmarkdown-rmeetup-2012](https://github.com/jeromyanglim/rmarkdown-rmeetup-2012/issues/4)
* [Add control over images with Markdown (#21189) · Issues · GitLab.org / GitLab Community Edition · GitLab](https://gitlab.com/gitlab-org/gitlab-ce/issues/21189)

---

### HTML in Markdown
You can put some html tags in [GFM](https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown) and github will render it.

More info https://github.com/github/markup/issues/245

```
h1 h2 h3 h4 h5 h6 h7 h8 br b i strong em a pre code img tt
div ins del sup sub p ol ul table thead tbody tfoot blockquote
dl dt dd kbd q samp var hr ruby rt rp li tr td th s strike summary details
```

<img height="120" width="120" src="http://htmlreference.io/images/boat.jpg">

`<img src="data/logo.jpg" width=25% align="right" />`

<details>
  <summary>Read more</summary>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra nec nulla vitae mollis.</p>
</details>

<dl>
  <dt>Web</dt>
  <dd>The part of the Internet that contains websites and web pages</dd>
  <dt>HTML</dt>
  <dd>A markup language for creating web pages</dd>
  <dt>CSS</dt>
  <dd>A technology to make HTML look better</dd>
</dl>

---

### Youtube videos

They can't be added directly but you can add an image with a link to the video like this:

```html
<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
```

Or, in pure Markdown, but losing the image sizing and border:

```
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
```

---

### Copy link as markdown bookmarklet
add this url to your browser bookmarks. Then click on it anytime you wand to get current link in markdown format.
`javascript:var text='['+document.title+']('+location.href+')';window.prompt("Copy to clipboard: Ctrl+C, Enter",text);void(0);`

---

[`this is code`](https://this_is_url/)

---

### `<a>` inside `<pre>`
<pre>
  <a href="http://htmlreference.io">HTML Reference</a>
</pre>

---

# Browser tabs to markdown lists
## Bookmarklet
save current tab title and url to markdown link: `- [title](url)`

create a new bookmark in your browser and paste as a link the follofing:
```js
javascript:var%20text='-%20%5B'+document.title+'%5D('+location.href+')';window.prompt(%22Copy%20to%20clipboard:%20Ctrl+C,%20Enter%22,text);void(0);
```

or without hyphen: (just `[title](url)`)
```js
javascript:var text='['+document.title+']('+location.href+')';window.prompt("Copy to clipboard: Ctrl+C, Enter",text);void(0);
```

## All safari tabs to markdown list
Simple script for macOS Script Editor that converts all Safari tabs to markdown links (copies to clipboard)

Paste following in macOS Script Editor, set javascript language, and run:
```js
var Safari = Application('Safari');
var tabs = Safari.windows[0].tabs;

var app = Application.currentApplication();
app.includeStandardAdditions = true;

var text = '';

for (var i = 0; i < tabs.length; i++) {
    text += '- [' + tabs[i].name() + '](' + tabs[i].url() + ')\n';
}


app.setTheClipboardTo(text);
app.displayNotification('Tabs converted to markdown list and copied to clipboard');
```
## Chrome tabs
there are nice extensions: 
- [Copy as Markdown - Chrome Web Store](https://chrome.google.com/webstore/detail/copy-as-markdown/fkeaekngjflipcockcnpobkpbbfbhmdn)
- [TabAttack - Chrome Web Store](https://chrome.google.com/webstore/detail/tabattack/ginflokhdahakklidfjlogllkkhokidj)
