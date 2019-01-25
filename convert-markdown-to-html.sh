#!/bin/bash

# take every path in the repo ending in .md
cd Pages
rm *.html
for infile in *md; do
    touch temp.md
    # add links to home index at top and bottom of page
    printf '[Home](../index.html)\n\n' > temp.md
    cat "$infile" >> temp.md
    printf '\n[Home](../index.html)' >> temp.md
    # derive output file name (replace .md with .html)
    outfile=`echo $infile | sed 's/md$/html/g'`
    # perform the conversion from MD to HTML, linking CSS in the process
    pandoc temp.md --webtex -o "$outfile"
    # add css file to first line of the file
    sed -i '1i<link rel="stylesheet" href="markdown.css" />' "$outfile"
    rm temp.md
done
cd ..

