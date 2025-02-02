(defn main
  [s]
  (->> (iterate #(rest %) (seq s))
       (take (inc (count s)))
       (map #(take-while #{\A \T \G \C} %))
       (map count)
       (apply max)))

(println (main (read-line)))
