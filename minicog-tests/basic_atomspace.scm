;; Basic AtomSpace Test Script
;; This script demonstrates fundamental operations with AtomSpace

;; Load the necessary modules
(use-modules (opencog))
(use-modules (opencog exec))

;; Clear the AtomSpace for a fresh start
(clear)

;; Create some basic atoms (nodes)
(define person (ConceptNode "Person"))
(define alice (ConceptNode "Alice"))
(define bob (ConceptNode "Bob"))

;; Create relationships (links)
(define alice-is-person (InheritanceLink alice person))
(define bob-is-person (InheritanceLink bob person))

;; Add some values to atoms
(cog-set-value! alice (PredicateNode "age") (FloatValue 25))
(cog-set-value! bob (PredicateNode "age") (FloatValue 30))

;; Display our knowledge
(display "AtomSpace contents:\n")
(cog-pprint-atomspace)

;; Simple query: Find all Person instances
(display "\nQuerying for all Person instances:\n")
(define all-persons 
  (Get
    (InheritanceLink
      (Variable "$x")
      person)))

;; Execute the query and display results
(display "Query results:\n")
(cog-execute! all-persons)

;; Access values
(display "\nAlice's age: ")
(display (cog-value alice (PredicateNode "age")))
(newline)

(display "\nAtomSpace size: ")
(display (cog-count-atoms))
(newline)

;; Exit with a message
(display "\nBasic AtomSpace test completed successfully.\n")