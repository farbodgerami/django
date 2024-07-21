import React from 'react'

const Rating = ({value,text,color}) => {
    return (
        <div className='rating'>
            {value}
            <span>
                <i style={{color}} className={
                    value>=1 ?'fas fa-star':value>=0.5?'fa fa-star-half-alt':'far fa-star'
                } >1</i>
            </span>
            <span>
                <i style={{color}} className={
                    value>=2 ?'fas fa-star':value>=1.5?'fa fa-star-half-alt':'far fa-star'
                } >1</i>
            </span>
            <span>
                <i style={{color}} className={
                    value>=3 ?'fas fa-star':value>=2.5?'fa fa-star-half-alt':'far fa-star'
                } >1</i>
            </span>
            <span>
                <i style={{color}} className={
                    value>=4 ?'fas fa-star':value>=3.5?'fa fa-star-half-alt':'far fa-star'
                } >1</i>
            </span>
            <span>
                <i style={{color}} className={
                    value>=5 ?'fas fa-star':value>=4.5?'fa fa-star-half-alt':'far fa-star'
                } >1</i>
            </span>
            <span>{text && text}</span>
        </div>
    )
}

export default Rating
