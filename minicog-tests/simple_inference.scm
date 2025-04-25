;; Simple Inference Test Script
;; This script demonstrates basic inference using URE

;; Load the necessary modules
(use-modules (opencog))
(use-modules (opencog exec))
(use-modules (opencog rule-engine))

;; Clear the AtomSpace for a fresh start
(clear)

;; Define some concept nodes for our knowledge base
(define human (ConceptNode "Human"))
(define mortal (ConceptNode "Mortal"))
(define socrates (ConceptNode "Socrates"))
(define plato (ConceptNode "Plato"))

;; Define our knowledge base with relationships
;; All humans are mortal
(define humans-are-mortal
  (ImplicationLink
    human
    mortal))

;; Socrates is human
(define socrates-is-human
  (InheritanceLink 
    socrates
    human))

;; Plato is human
(define plato-is-human
  (InheritanceLink
    plato
    human))

;; Display our initial knowledge base
(display "Initial Knowledge Base:\n")
(cog-pprint-atomspace)

;; Define a simple deduction rule
(define deduction-rule
  (BindLink
    (VariableList
      (TypedVariableLink
        (VariableNode "$A")
        (TypeNode "ConceptNode"))
      (TypedVariableLink
        (VariableNode "$B")
        (TypeNode "ConceptNode"))
      (TypedVariableLink
        (VariableNode "$C")
        (TypeNode "ConceptNode")))
    (AndLink
      (InheritanceLink
        (VariableNode "$A")
        (VariableNode "$B"))
      (ImplicationLink
        (VariableNode "$B")
        (VariableNode "$C")))
    (InheritanceLink
      (VariableNode "$A")
      (VariableNode "$C"))))

;; Create a simple rule base (ruleset)
(define rule-base (ConceptNode "simple-deduction-rule-base"))
(ure-add-rules rule-base (list (cons deduction-rule (NumberNode 1))))

;; Configure the rule engine
(ure-set-maximum-iterations rule-base 20)
(ure-set-fc-retry-exhausted-sources rule-base #t)

;; Apply forward chaining to see if we can infer Socrates is mortal
(display "\nRunning forward chaining inference...\n")
(define results (cog-fc rule-base socrates-is-human))

;; Check if we successfully inferred that Socrates is mortal
(display "Checking if we inferred Socrates is mortal:\n")
(define socrates-is-mortal 
  (InheritanceLink 
    socrates
    mortal))

(if (cog-link? socrates-is-mortal)
    (display "Success! Inferred that Socrates is mortal.\n")
    (display "Failed to infer that Socrates is mortal.\n"))

;; Now try to infer that Plato is mortal
(display "\nRunning inference for Plato...\n")
(define plato-results (cog-fc rule-base plato-is-human))

;; Check if we successfully inferred that Plato is mortal
(display "Checking if we inferred Plato is mortal:\n")
(define plato-is-mortal 
  (InheritanceLink 
    plato
    mortal))

(if (cog-link? plato-is-mortal)
    (display "Success! Inferred that Plato is mortal.\n")
    (display "Failed to infer that Plato is mortal.\n"))

;; Display our knowledge base after inference
(display "\nKnowledge Base After Inference:\n")
(cog-pprint-atomspace)

(display "\nSimple inference test completed.\n")