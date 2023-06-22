


while true; do
    python3 tor.py &
    PID=$!

    sleep 120

    if ps -p "$PID" > /dev/null; then
        kill "$PID"
        echo "Python script terminated."
    else
        echo "Python script is not running."
    fi

    # Add a delay before the next iteration if needed
    sleep 3
done
