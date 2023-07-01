while read line || [[ -n "$line" ]]; do
    IFS=' ' read -r -a array <<< "$line"
    limit="${array[2]}"
    fizz="${array[0]}"
    buzz="${array[1]}"
    result=""

    for ((i=1; i <= $limit; i++)); do
        if (( $i%$fizz == 0)) && (( $i%$buzz == 0)); then
            result="$result FB"
            continue
        fi
        if (( $i%$fizz == 0)); then
            result="$result F"
            continue
        fi
        if (( $i%$buzz == 0)); then
            result="$result B"
            continue
        fi
        result="$result $i"
    done
    echo $result
done < $1