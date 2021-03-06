HPMOR -- Annotated
===================

LaTeX/PDF version of “Harry Potter and the Methods of Rationality” -- with annotations to highlight foreshadowing.

HPMOR has lots of foreshadowing that rewards repeated reading. This fork adds annotations meant to highlight clever foreshadowing, for example in Chapter 1:

---

![Foreshadowing text](Pictures/foreshadow-ex1.png)

...

![Foreshadowing footnote](Pictures/foreshadow-ex2.png)

---

The LaTeX code to generate these notes is simply

    sick for weeks\hint{We learn in Ch 17 that ...}

To link between places in the text, use `\mylabel` and `\pageref`. For example: In Ch 17:

```latex
    Dumbledore was laughing now.\hint{Dumbledore is laughing because 
       he realizes blah blah, see page~\pageref{dd-laughs2}}
    \mylabel{dd-laughs}
```

And in Ch 110: 

```latex
    When I saw you had made a Good Voldemort to oppose the evil one---ah, how I laughed!
    \hint{The scene: page~\pageref{dd-laughs}}
    \mylabel{dd-laughs2}
```

- The `hint{}` macro in `hp-header.tex` can be configured to place the numbers and footnote text in various positions: in the margins (as shown above), within the text body, at the end of the chapter, etc.
- I commented-out the PDF covers because I intend to print my own hard-copies through [lulu.com](https://www.lulu.com/) using the method described by  <https://github.com/ianstormtaylor/hpmor>.


Want to help? Help me integrate the foreshadowing threads from the [hpmor subreddit](https://www.reddit.com/r/hpmor), e.g., 

- https://www.reddit.com/r/HPMOR/comments/2zgvhf/spoilers_for_chapter_46_more_foreshadowing_that_i/
- https://www.reddit.com/r/HPMOR/comments/4on1vu/whats_your_favorite_example_of_foreshadowing/
- https://www.reddit.com/r/HPMOR/comments/2wcmyd/hpmor_annotated_a_new_sequencebased_attempt/
- https://www.reddit.com/r/HPMOR/comments/22nm13/hpmor_annotated_wiki_come_help_out/
- https://www.reddit.com/r/HPMOR/comments/tvx96/annotated_hpmor_file_anyone/
- [more...](https://www.google.com/search?q=annotation+site%3Areddit.com%2Fr%2Fhpmor)
- [and more...](https://www.google.com/search?q=foreshadowing+site%3Areddit.com%2Fr%2Fhpmor)




README forked from rjl20
=========================


This fork incorporates changes made to the chapters after they were added to 
the PDF. Chapter 9, for example, has had a large chunk moved to the 
"Omake Files" chapter since it was first published, due to reader reactions.
Other chapters have had significant changes made in order to work with later
chapters as they were written. Because the PDF conversion was a manual process,
few of these changes were reflected in the PDF until now.


Files
=====

* hpmor.tex - the main file
* hp-format.tex - mostly set up memoir
* hp-hacks.tex - all sorts of formatting commands used in the text
* new-chapters/ - one file per chapter, included from hpmor.tex
* chapters/ - one file per chapter, the original files before my fork
* out/ - generated files are put here, including the main output, hpmor.pdf
* pkg/ - some latex packages that might be tricky to find
* xfonts/ - the various fonts used
* Makefile - use "make" to build the full PDF, "make all" to build the full PDF and all six sub-books, and "make clean" to clean up. "make hpmor-N.pdf", where N is an integer from 1 through 6, will build just that sub-book.



Contributing
============

If you'd like to help, the files to edit are in new-chapters/. 

NB: I've moved the Omake Files chapters (11 and 64) to the end of the PDF. Those chapter 
numbers are omitted in the text, so chapter 10 is followed by chapter 12, for example.
In the sub-book PDFs, all chapters are renumbered to start from 1 at the start of a book,
and there are no appendices.

