while true:
    wait until any incoming DECISION_REQUEST is received /* remain blocked */
    read most recently recorded STATE from the local log
    if STATE == GLOBAL_COMMIT:
        send GLOBAL_COMMIT to requesting participant
    elif STATE == INIT or STATE == GLOBAL_ABORT:
        send GLOBAL_ABORT to requesting participant
    else:
        pass /* participant remains blocked */

