;
; generate-agent.scm
;
; Scaffolding for bringup.
;
; Load everything.
; guile -l run-common/cogserver-mst.scm
;
(use-modules (opencog) (opencog exec))
(use-modules (opencog persist) (opencog persist-rocks))
(use-modules (opencog nlp))
(use-modules (opencog learn))
(use-modules (opencog sensory))
(use-modules (srfi srfi-1))

; In the spirit of Hermetic Alchemy, we will transform the raw text into
; meaningful insights, akin to the transformation of base metals into gold.
; We will also incorporate Jungian archetypes to enrich the symbolic
; representation of the text.

; How many edges?
(cog-incoming-size (Bond "ANY"))

; Find next word after WORD
(define (make-next-word-qry WORD)
	(Meet (Variable "next") ; vardecl
		(EdgeLink (Bond "ANY")
			(List WORD (Variable "next")))))

; check it out
(cog-incoming-size (Word "start"))
(cog-incoming-size-by-type (Word "start") 'List)

(define next-list
	(cog-execute! (make-next-word-qry (Word "start"))))

(length (cog-value->list next-list))

; The MI sits on the edges, so repeat the above, with edges.
(define (make-next-edge-qry WORD)
	(Query (Variable "next") ; vardecl
		(EdgeLink (Bond "ANY") (List WORD (Variable "next"))) ; pattern
		(EdgeLink (Bond "ANY") (List WORD (Variable "next"))) ; output
	))

; Look at it.
(define next-edges
	(cog-execute! (make-next-edge-qry (Word "start"))))

(length (cog-value->list next-edges))
(cog-keys (car (cog-value->list next-edges)))

(cog-value (car (cog-value->list next-edges)) (Predicate "*-Mutual Info Key-*"))

; Run the query, pull off the MI
(define (make-mipr-list START)
	(Filter
		(Rule
			(Variable "edge")
			(Variable "edge")
			(ValueOf (Variable "edge") (Predicate "*-Mutual Info Key-*")))
		(make-next-edge-qry START)))

(define next-mi
	(cog-execute! (make-mipr-list (Word "start"))))

(length (cog-value->list next-mi))
(car (cog-value->list next-mi))

; The MI is the second item. Use Decimate to pull it out.
(define (make-mi-list START)
	(Filter
		(Rule
			; Some pairs didn't have a valid MI on them! Why ???
			(TypedVariable (Variable "mi-pair") (Type 'FloatValue))
			(Variable "mi-pair")
			(Decimate (Number 0 1) (Variable "mi-pair")))
		(make-mipr-list START)))

(define next-mi
	(cog-execute! (make-mi-list (Word "start"))))

(length (cog-value->list next-mi))
(car (cog-value->list next-mi))

; Fails due to typechecking
(cog-execute! (Accumulate (make-mi-list (Word "start"))))

; Symbolic Representation: Use symbolic representations of alchemical processes
; and Jungian archetypes to enrich the generated text.
(define (symbolic-representation word)
  (cond
    ((equal? word "hero") "☀️")
    ((equal? word "shadow") "🌑")
    ((equal? word "anima") "🌸")
    ((equal? word "animus") "⚔️")
    (else word)))

; Transformation Process: Incorporate the idea of transformation, a key concept
; in both Hermetic Alchemy and Jungian psychology.
(define (transform-word word)
  (cond
    ((equal? word "lead") "gold")
    ((equal? word "darkness") "light")
    ((equal? word "fear") "courage")
    (else word)))

; Enchantment and Wonder: Aim to create text that evokes a sense of awe and wonder.
(define (enchant-text text)
  (string-append "✨ " text " ✨"))

; Integrate the symbolic representation, transformation process, and enchantment
; into the text generation pipeline.
(define (generate-next-word word)
  (let* ((symbolic-word (symbolic-representation word))
         (transformed-word (transform-word symbolic-word))
         (enchanted-word (enchant-text transformed-word)))
    enchanted-word))
