(defn int-input [] (Long/parseLong (read-line)))
(defn int-list-input [] (map #(Long/parseLong %) (clojure.string/split (read-line) #" ")))
(defn int-row-input [n] (line-seq))

#_(defn main
    [a]
    (->> a
         (map-indexed (fn [idx item] [idx item]))
         (sort-by second >)
         second
         first
         inc))

#_(println
   (let [n (int-input)
         a (map #(bigint %) (clojure.string/split (read-line) #" "))]
     (main a)))

(println (int-list))
