;; Pattern Matching Test Script
;; This script demonstrates pattern matching in AtomSpace

;; Load necessary modules
(use-modules (opencog))
(use-modules (opencog exec))

;; Clear the AtomSpace for a fresh start
(clear)

;; Create a simple knowledge base about animals
(define mammal (ConceptNode "Mammal"))
(define bird (ConceptNode "Bird"))
(define fish (ConceptNode "Fish"))

;; Add some specific animals
(define dog (ConceptNode "Dog"))
(define cat (ConceptNode "Cat"))
(define sparrow (ConceptNode "Sparrow"))
(define eagle (ConceptNode "Eagle"))
(define salmon (ConceptNode "Salmon"))

;; Define relationships
(InheritanceLink dog mammal)
(InheritanceLink cat mammal)
(InheritanceLink sparrow bird)
(InheritanceLink eagle bird)
(InheritanceLink salmon fish)

;; Add some properties
(EvaluationLink 
  (PredicateNode "has_fur") dog)
(EvaluationLink 
  (PredicateNode "has_fur") cat)
(EvaluationLink 
  (PredicateNode "has_feathers") sparrow)
(EvaluationLink 
  (PredicateNode "has_feathers") eagle)
(EvaluationLink 
  (PredicateNode "has_scales") salmon)
(EvaluationLink 
  (PredicateNode "can_fly") eagle)
(EvaluationLink 
  (PredicateNode "can_fly") sparrow)
(EvaluationLink 
  (PredicateNode "can_swim") salmon)
(EvaluationLink 
  (PredicateNode "can_swim") dog)

;; Display our knowledge base
(display "Knowledge Base:\n")
(cog-pprint-atomspace)

;; Define a simple pattern to find all mammals
(display "\nFinding all mammals:\n")
(define find-mammals
  (GetLink
    (InheritanceLink
      (Variable "$animal")
      mammal)))

(cog-execute! find-mammals)

;; More complex pattern: Find all animals that can fly
(display "\nFinding all flying animals:\n")
(define find-flying-animals
  (GetLink
    (AndLink
      (InheritanceLink
        (Variable "$animal")
        (TypeChoice mammal bird fish))
      (EvaluationLink
        (PredicateNode "can_fly")
        (Variable "$animal")))))

(cog-execute! find-flying-animals)

;; Find animals that have a specific property and belong to a category
(display "\nFinding all mammals with fur:\n")
(define find-furry-mammals
  (GetLink
    (AndLink
      (InheritanceLink
        (Variable "$animal")
        mammal)
      (EvaluationLink
        (PredicateNode "has_fur")
        (Variable "$animal")))))

(cog-execute! find-furry-mammals)

;; Pattern with multiple variables - find relationships between animals and their features
(display "\nFinding animal-feature relationships:\n")
(define animal-features
  (GetLink
    (AndLink
      (InheritanceLink
        (Variable "$animal")
        (Variable "$category"))
      (EvaluationLink
        (Variable "$feature")
        (Variable "$animal")))))

;; Execute the complex query (limit output due to potential size)
(define results (cog-execute! animal-features))
(display "Found relationships (showing first results):\n")
(cog-value->list results)

(display "\nPattern matching tests completed successfully.\n")