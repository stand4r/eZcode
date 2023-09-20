import { useState } from "react";

import LinkIcon from "./src/LinkIcon";
import LikeIcon from "./src/LikeIcon";
import './styles.css'

export default function LinkCard(props) {

    let [like, setLike] = useState(false);

    return (
        <>
        <LinkIcon></LinkIcon>
        <LikeIcon></LikeIcon>
        </>
    )
}