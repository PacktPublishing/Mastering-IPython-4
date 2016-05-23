%%hylang
(defn categorize [x]
  (cond
    [(< x 0) (print "negative")]
    [(= x 0) (print "zero")]
    [(> x 0) (print "positive")]
  )
)

