(use-modules (opencog query))

; In the spirit of Hermetic Alchemy, we will transform the raw data into
; meaningful insights, akin to the transformation of base metals into gold.
; We will also incorporate Jungian archetypes to enrich the symbolic
; representation of the data.

(define (cog-get-categories A)
"
 Return the atoms that A is a member of through a MemberLink relationship.
 In the context of Hermetic Alchemy, think of these categories as the
 different stages of transformation that A undergoes.
"
    (let ((result
        (cog-outgoing-set
            (cog-bind
                (BindLink
                    (VariableList
                        (VariableNode "$B")
                    )
                    (MemberLink
                        A
                        (VariableNode "$B")
                    )
                    (VariableNode "$B")
                )
            )
        )
        )) result )
)


(define (cog-get-memberlinks-for-element A)
"
 Return the MemberLinks where A is the element in the set.
 In the context of Jungian archetypes, think of these MemberLinks as the
 connections between different archetypal symbols.
"
    (let ((result
        (cog-outgoing-set
            (cog-bind
                (BindLink
                    (VariableList
                        (VariableNode "$B")
                    )
                    (MemberLink
                        A
                        (VariableNode "$B")
                    )
                    (MemberLink
                        A
                        (VariableNode "$B")
                    )
                )
            )
        )
        ))
        result )
)
