
;;; ============================================================================
;;; 8-EMBODIMENT: Sensorimotor Integration
;;; ============================================================================
;;; Advanced sensorimotor integration and embodied cognition
;;; ============================================================================

(use-modules (opencog)
             (opencog exec)
             (opencog query))

;;; Sensorimotor system
(define-public sensorimotor-system
  (ConceptNode "sensorimotor-system"))

;;; Integrate sensorimotor
(define-public (integrate-sensorimotor)
  "Integrate sensorimotor capabilities"
  (SequentialAndLink
    (ExecutionLink (GroundedSchemaNode "scm: initialize-sensory-processing"))
    (ExecutionLink (GroundedSchemaNode "scm: setup-motor-control"))
    (ExecutionLink (GroundedSchemaNode "scm: enable-embodied-cognition"))))

;;; Initialize sensory processing
(define-public (initialize-sensory-processing)
  "Initialize sensory processing systems"
  (ListLink
    (ConceptNode "visual-processing")
    (ConceptNode "auditory-processing")
    (ConceptNode "tactile-processing")))

;;; Setup motor control
(define-public (setup-motor-control)
  "Setup motor control systems"
  (EvaluationLink
    (PredicateNode "motor-control-active")
    (ListLink sensorimotor-system)))

(export integrate-sensorimotor
        initialize-sensory-processing
        setup-motor-control)
