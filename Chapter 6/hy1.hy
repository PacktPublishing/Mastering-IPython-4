%%hylang
(import math)
(defn safesqrt [x]
  (if (< x 0)
    (math.sqrt (- 0 x))
    (math.sqrt x)
  )
)
