# The haiku — how it was chosen

Ten candidates, each counted syllable by syllable to the strict 5-7-5
shape, each at most 200 characters. The judge weighs, most important first:
the form holds, the picture at the centre is concrete and fresh, the last
line turns the poem, and every word earns its place. Clichés were avoided:
no "works on my machine", no generic moaning about bugs.

## Candidates

### 1. The blinking cursor
> three a.m. cursor
> blinks on the last log line still
> and the bug waves back
- Line 1: three(1) a.m.(2) cur-sor(2) = 5
- Line 2: blinks(1) on(1) the(1) last(1) log(1) line(1) still(1) = 7
- Line 3: and(1) the(1) bug(1) waves(1) back(1) = 5
- Verdict: concrete, but "waves back" is cute rather than true; the turn
  is a shrug.

### 2. The one red test
> one last test stays red
> two hundred green around it
> it was a typo
- Line 1: one(1) last(1) test(1) stays(1) red(1) = 5
- Line 2: two(1) hun-dred(2) green(1) a-round(2) it(1) = 7
- Line 3: it(1) was(1) a(1) ty-po(2) = 5
- Verdict: very true to debugging, and the turn lands — but "typo" is the
  first answer every debugger reaches for; not fresh enough.

### 3. Past me says sorry — CHOSEN
> the stack trace ends here
> in a file I never wrote
> past me says sorry
- Line 1: the(1) stack(1) trace(1) ends(1) here(1) = 5
- Line 2: in(1) a(1) file(1) I(1) nev-er(2) wrote(1) = 7
- Line 3: past(1) me(1) says(1) sor-ry(2) = 5
- 68 characters including the two newlines. Verdict: the centre is the most
  concrete image of the ten — a stack trace, a real file, and the disowning
  shock of finding it is code you do not recognise. The last line turns the
  poem: the culprit is not a stranger, it is past-me, and past-me apologises.
  Every word earns its place; nothing is decoration.

### 4. Null again
> breakpoint at line nine
> the value is null again
> so is my weekend
- Line 1: break-point(2) at(1) line(1) nine(1) = 5
- Line 2: the(1) val-ue(2) is(1) null(1) a-gain(2) = 7
- Line 3: so(1) is(1) my(1) week-end(2) = 5
- Verdict: funny and concrete, but the turn is a complaint about the
  weekend, not about the code.

### 5. The hiding comma
> cursor blinks at three
> the log scrolls past like night rain
> one comma hides still
- Line 1: cur-sor(2) blinks(1) at(1) three(1) = 5
- Line 2: the(1) log(1) scrolls(1) past(1) like(1) night(1) rain(1) = 7
- Line 3: one(1) com-ma(2) hides(1) still(1) = 5
- Verdict: lovely middle image, but the last line fizzles — "hides still"
  says nothing new.

### 6. The one space
> my debug prints bloom
> like weeds through the whole codebase
> the bug was one space
- Line 1: my(1) de-bug(2) prints(1) bloom(1) = 5
- Line 2: like(1) weeds(1) through(1) the(1) whole(1) code-base(2) = 7
- Line 3: the(1) bug(1) was(1) one(1) space(1) = 5
- Verdict: strong turn, genuinely true — but "one space" leans on the same
  typo family as candidate 2.

### 7. Off by one
> off by one again
> the loop eats the last row whole
> my lunch can wait then
- Line 1: off(1) by(1) one(1) a-gain(2) = 5
- Line 2: the(1) loop(1) eats(1) the(1) last(1) row(1) whole(1) = 7
- Line 3: my(1) lunch(1) can(1) wait(1) then(1) = 5
- Verdict: the middle line is vivid, but the turn is about lunch, not the
  bug.

### 8. Morning ships the bug
> three a.m. and the
> the stack trace glows on my face
> morning ships the bug
- Line 1: three(1) a.m.(2) and(1) the(1) = 5
- Line 2: the(1) stack(1) trace(1) glows(1) on(1) my(1) face(1) = 7
- Line 3: morn-ing(2) ships(1) the(1) bug(1) = 5
- Verdict: atmospheric, but "three a.m. and the" is a weak opening line —
  it leans on the next line to mean anything.

### 9. The semicolon
> a semicolon
> hides between two lines of sleep
> the whole build turns green
- Line 1: a(1) sem-i-co-lon(4) = 5
- Line 2: hides(1) be-tween(2) two(1) lines(1) of(1) sleep(1) = 7
- Line 3: the(1) whole(1) build(1) turns(1) green(1) = 5
- Verdict: a neat turn — one character fixes everything — but the centre
  image (a semicolon hiding) is less concrete than a stack trace or a log.

### 10. The waiting breakpoint
> the breakpoint waits still
> for a value that won't come
> I wrote it at noon
- Line 1: the(1) break-point(2) waits(1) still(1) = 5
- Line 2: for(1) a(1) val-ue(2) that(1) won't(1) come(1) = 7
- Line 3: I(1) wrote(1) it(1) at(1) noon(1) = 5
- Verdict: patient and true, but the turn ("I wrote it at noon") is a
  footnote, not a turn.

## Why #3 wins

It is the only candidate where all four of the judge's weights land at once:
the 5-7-5 form holds exactly; the centre is concrete (a stack trace, a
file); the last line turns the poem (the stranger's code is mine, and it
apologises); and no word is spare — "ends here" sets the scene, "never
wrote" carries the disowning, "says sorry" is the whole joke and the whole
truth of debugging in two syllables.
