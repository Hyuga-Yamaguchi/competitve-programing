(defn count-divisor
  [n]
  (count (filter #(zero? (mod n %)) (range 1 (inc n)))))

(defn main
  [n]
  (count (filter #(= 8 (count-divisor %)) (range 1 (inc n) 2))))

(defn int-input
  []
  (Double/parseDouble (read-line)))

(println (main (int-input)))
