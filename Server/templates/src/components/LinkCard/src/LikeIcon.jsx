import { useState } from "react"
export default function LikeIcon() {
    let [like, setlike] = useState(false);
    return (
        <svg width="28.166687" height="24.385132" viewBox="0 0 28.1667 24.3851" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns: xlink="http://www.w3.org/1999/xlink" onClick={() => {setlike(!like);}}>
            <defs />
            <path id="path" d="M0.75 8.08337C0.75 15.4166 9.41669 22.0834 14.0833 23.6342C18.75 22.0834 27.4167 15.4166 27.4167 8.08337C27.4167 4.03333 24.1334 0.75 20.0833 0.75C17.6031 0.75 15.4105 1.98132 14.0833 3.86584C12.7562 1.98132 10.5635 0.75 8.08331 0.75C4.03326 0.75 0.75 4.03333 0.75 8.08337Z" stroke = { !like ? "#808080" : "none"} fill = { like ? "#0061FF" : "none"} />
        </svg>
    )
}