Generating output
=================
Design notes for generating output text. Two ideas: use LG and use dorky
pairs.

## LG generation
Generate text with Link Grammar. This is the correct long-term solution,
but requires some fair amount of work on the LG side and on the
`lg-atomese` modules, and here. So for proof-of-concept, just skip this
for now.
```
link-generator -c 4 -k 4 -l en
link-generator -l en -s 0
This is * test
echo 'This \* a te\* of \*.a sentence generation' | time link-generator -l en -s 0 --verbosity=2
echo 'This is a \*' | time link-generator -l en -s 0 --verbosity=2
```
Early versions would take prior string and just add one more star.
Or maybe two stars. Keep it short.

General issues:
* Allow link-parser app to special case wild-cards for generation.
* Loading of entire dict is unfeasible, so...
  Load only possible links?

Ideas:
* Parse given word seq containing blanks, use unknown word for
  blanks, then lookup all words with matching disjuncts. This
  requires:
* Allow dict lookup of words according to desired disjuncts.

OK, screw that. There are multiple design issues raised by above.

## Simple chaining
For quick bringup, lets just do simple chaining. Ideas in summary form:

1) Starting with a word A, use incoming set to randomly select some
subset of all possible edges. This will be called the "focus set" or the
"attentional focus". Because it is small, it can be exhaustively
iterated and sorted into high-to-low MI order. This provides a weighted
distribution, from which a rescaled uniform-random choice can be made.

2) Random sample N out of full incoming set.

Lets stream-process this: Query returns list of edges
```
	(Query (Variable "next") ; vardecl
      (EdgeLink (Predicate "ANY")
			(List (Word "start") (Variable "next"))))
```
This returns a list (a short list? where do we plug in N to cap the size?)
The list is actually a `QueueValue`.

3) Out of this queue Value, select one, with the proper weighting.
   Treating this as a collection of priors requires a sum over all elts
   in the queue, to obtain a total norm, and then making a second pass
   to choose one for this weighted distribution. This requires a
   "non-local" RAM-walking sum.

3a) Create a pipeline elt that takes list, adds the weights, then
    selects N random items from that weighted list.

3b) A local way of doing this is to pick a min-MI cutoff, and selecting
    the first elt that is above the cutoff.

3c) A quasi-local way is to take the average of the first three elts,
    the first K elts, and then accept the first that is above this average.
    So the first K are always discarded, until the moving average is arrived
    at.

This needs:
4) Atomese to fish out/Filter the MI from the correct location
   and or compute it on the fly.

   Atomese to compute a moving average.

What is the minimal way to do this?
Can it be done so that MOSES can be applied to tune it?

Ugh.

## Integrating Hermetic Alchemy and Jungian Archetypes
To integrate the concepts of Hermetic Alchemy and Jungian archetypes into the text generation process, we can follow these steps:

1) **Symbolic Representation**: Use symbolic representations of alchemical processes and Jungian archetypes to enrich the generated text. For example, words and phrases can be associated with archetypal symbols like the Hero, the Shadow, the Anima/Animus, etc.

2) **Transformation Process**: Incorporate the idea of transformation, a key concept in both Hermetic Alchemy and Jungian psychology. This can be done by creating functions that transform words and phrases based on alchemical principles (e.g., turning base words into "golden" words) and archetypal transformations (e.g., the Hero's journey).

3) **Enchantment and Wonder**: Aim to create text that evokes a sense of awe and wonder. This can be achieved by using poetic and mystical language, drawing inspiration from alchemical texts and Jungian literature.

### Example Implementation
Here is an example of how these concepts can be integrated into the text generation process:

1) **Symbolic Representation**:
```scheme
(define (symbolic-representation word)
  (cond
    ((equal? word "hero") "☀️")
    ((equal? word "shadow") "🌑")
    ((equal? word "anima") "🌸")
    ((equal? word "animus") "⚔️")
    (else word)))
```

2) **Transformation Process**:
```scheme
(define (transform-word word)
  (cond
    ((equal? word "lead") "gold")
    ((equal? word "darkness") "light")
    ((equal? word "fear") "courage")
    (else word)))
```

3) **Enchantment and Wonder**:
```scheme
(define (enchant-text text)
  (string-append "✨ " text " ✨"))
```

### Integrating with the Existing Pipeline
To integrate these functions into the existing text generation pipeline, we can modify the pipeline to include calls to `symbolic-representation`, `transform-word`, and `enchant-text` at appropriate stages.

For example, after selecting a word from the focus set, we can apply these transformations before generating the next word in the sequence.

```scheme
(define (generate-next-word word)
  (let* ((symbolic-word (symbolic-representation word))
         (transformed-word (transform-word symbolic-word))
         (enchanted-word (enchant-text transformed-word)))
    enchanted-word))
```

By incorporating these concepts, we can create a text generation process that not only produces coherent and meaningful text but also evokes a sense of enchantment and wonder, inspired by Hermetic Alchemy and Jungian archetypes.
