;; Unification Test Script
;; This script demonstrates the unification capabilities of MiniCog

;; Load the necessary modules
(use-modules (opencog))
(use-modules (opencog exec))
(use-modules (opencog unify)) ; Load the unify module

;; Clear the AtomSpace for a fresh start
(clear)

;; Create some patterns and expressions to demonstrate unification

;; Define some variables for our patterns
(define var-x (VariableNode "$x"))
(define var-y (VariableNode "$y"))
(define var-z (VariableNode "$z"))

;; Define some constants to use in our expressions
(define apple (ConceptNode "apple"))
(define banana (ConceptNode "banana"))
(define fruit (ConceptNode "fruit"))

;; Create a simple pattern with variables
(define pattern1
  (ListLink
    var-x
    (ConceptNode "is a")
    var-y))

;; Create an expression that should match the pattern
(define expr1
  (ListLink
    apple
    (ConceptNode "is a")
    fruit))

;; Create another pattern with nested structure
(define pattern2
  (ListLink
    var-x
    (ListLink
      var-y
      var-z)))

;; Create an expression for the nested pattern
(define expr2
  (ListLink
    apple
    (ListLink
      banana
      fruit)))

;; Display our patterns and expressions
(display "Patterns and Expressions:\n")
(display "Pattern 1: ")
(display pattern1)
(newline)
(display "Expression 1: ")
(display expr1)
(newline)
(display "Pattern 2: ")
(display pattern2)
(newline)
(display "Expression 2: ")
(display expr2)
(newline)

;; Create unifier links for testing
(define unifier1
  (UnifierLink
    (VariableList var-x var-y)
    pattern1
    expr1))

(define unifier2
  (UnifierLink
    (VariableList var-x var-y var-z)
    pattern2
    expr2))

;; Execute the unification and display results
(display "\nUnification Results:\n")

(display "Unifier 1 results:\n")
(cog-execute! unifier1)

(display "\nUnifier 2 results:\n")
(cog-execute! unifier2)

;; Test unification with type constraints
(define typed-var-x
  (TypedVariableLink
    var-x
    (TypeNode "ConceptNode")))

(define typed-var-y
  (TypedVariableLink
    var-y
    (TypeNode "ConceptNode")))

(define unifier-typed
  (UnifierLink
    (VariableList typed-var-x typed-var-y)
    pattern1
    expr1))

(display "\nTyped Unifier results:\n")
(cog-execute! unifier-typed)

;; Try a more complex example with a rule-like structure
(define rule-pattern
  (AndLink
    (InheritanceLink var-x var-y)
    (InheritanceLink var-y var-z)))

(define rule-instance
  (AndLink
    (InheritanceLink apple banana)
    (InheritanceLink banana fruit)))

(define rule-unifier
  (UnifierLink
    (VariableList var-x var-y var-z)
    rule-pattern
    rule-instance))

(display "\nRule Pattern Unifier results:\n")
(cog-execute! rule-unifier)

(display "\nUnification tests completed.\n")