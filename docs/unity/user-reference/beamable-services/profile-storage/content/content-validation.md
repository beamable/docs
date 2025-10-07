# Content - Validation

The content system supports optional validation for each field of a `ContentObject` subclass. This allows game makers to easily build tooling to facilitate team members with their content administration tasks.

Beamable provides **built-in validation** and also allows for **custom validation**.

**Content Validation Results**

| ContentObject (Valid) | ContentObject (Invalid) |
| :-------------------- | :---------------------- |
| ![Valid](../../../../../../../media/imgs/valid.png) | ![Invalid](../../../../../../../media/imgs/invalid.png) |

**Content Validation Types**

Here are the built-in validation types. Beamable also supports creating custom validation types.

All validation types must descend from [`ValidationAttribute`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1ValidationAttribute.html).

| Name | Detail |
|------|--------|
| [`CannotBeBlank`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1CannotBeBlank.html) | Ensures field value is NOT blank |
| [`CannotBeEmpty`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1CannotBeEmpty.html) | Ensures field value is NOT empty |
| [`MustBeComparatorString`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1MustBeComparatorString.html) | Ensures field value is ">", "\<", "=", etc... |
| [`MustBeCurrency`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1MustBeCurrency.html#details) | Ensures field value is a `CurrencyContent` |
| [`MustBeCurrencyOrItem`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1MustBeCurrencyOrItem.html#details) | Ensures field value is a `CurrencyContent` or `ItemContent` |
| [`MustBeDateString`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1MustBeDateString.html) | Ensures field value is a date string |
| [`MustBeItem`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1MustBeItem.html#details) | Ensures field value is an `ItemContent` |
| [`MustBeLeaderboard`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1MustBeLeaderboard.html#details) | Ensures field value is an `LeaderboardContent` |
| [`MustBeNonNegative`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1MustBeNonNegative.html#details) | Ensures field value is NOT negative |
| [`MustBeOneOf`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1MustBeOneOf.html) | Ensures field value is of a type contained in a given list of types |
| [`MustBePositive`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1MustBePositive.html) | Ensures field value is NOT negative |
| [`MustContain`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1MustContain.html) | Ensures field value contains certain string(s) |
| [`MustReferenceContent`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1MustReferenceContent.html) | Ensures field value is of type `ContentObject`. |

## Examples

**Code**

This snippet demonstrates usage and implementation of validation by subclassing [`ValidationAttribute`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1Validation_1_1ValidationAttribute.html).

!!! info "Code Example"

    • See code examples at [GitHub.com/Beamable_SDK_Examples](https://www.Github.com/beamable/Beamable_SDK_Examples/)

**Content Validation Usage**

This `ContentValidationExample.cs` snippet demonstrates the usage of built-in validation and custom validation within a custom subclass of `ContentObject`.

ComplexItem.cs
```csharp
using System;
using Beamable.Common.Content;
using Beamable.Common.Content.Validation;
using Beamable.Common.Inventory;

namespace Beamable.Examples.Services.ContentService
{
    [Serializable]
    public class ComplexItemLink : ContentLink<ComplexItem> {}

    /// <summary>
    /// This demonstrates validation rules
    /// for use with any fields within a <<see cref="ContentObject"/>
    /// subclass.
    ///
    /// Using validation is optional.
    ///
    /// See "Beamable.Common.Content.Validation" for full list.
    /// 
    /// </summary>
    [ContentType("complex_item")]
    public class ComplexItem : ItemContent
    {
        /// <summary>
        /// Built-in: Validation requires that the value be NOT blank.
        /// </summary>
        [CannotBeBlank]
        public string Name = "";
        
        /// <summary>
        /// Custom: Validation requires that the value be string and of
        /// string length of 2 or 3.
        /// See <see cref="MustBeStringLength"/>.
        /// </summary>
        [MustBeStringLength (2, 3)]
        public string FavoriteLetters = "";
        
        /// <summary>
        /// Built-in: Validation requires that the value be positive and
        /// non-zero.
        /// </summary>
        [MustBePositive(false)]
        public int Defense = 0;

        /// <summary>
        /// Built-In: Here is an optional value with no validation.
        /// </summary>
        public OptionalInt Health;
    }
}
```

**Content Validation Implementation**

This `MustBeStringLength.cs` snippet demonstrates the implementation of **custom** validation.

MustBeStringLength.cs
```csharp
using System;
using Beamable.Common.Content;
using Beamable.Common.Content.Validation;

namespace Beamable.Examples.Services.ContentService
{
    /// <summary>
    /// Demonstrates a custom validation rule for a
    /// field of a <see cref="ContentObject"/> subclass.
    /// </summary>
    public class MustBeStringLength : ValidationAttribute
    {
        //  Fields  ---------------------------------------
        private const string STRING_TYPE = "Value must be a string type.";
        private const string ARGUMENT_ERROR = "The StringLengthMin of {0} must be <= StringLengthMax of {1}.";
        private const string VALUE_ERROR = "The field string length of {0} must be >= {1} and <= {2}.";
        private int _stringLengthMin = 0;
        private int _stringLengthMax = 0;

        //  Constructor Methods  --------------------------------
        
        /// <summary>
        /// Optional. Pass validation arguments.
        /// </summary>
        /// <param name="stringLengthMin"></param>
        /// <param name="stringLengthMax"></param>
        public MustBeStringLength(int stringLengthMin, int stringLengthMax)
        {
            _stringLengthMin = stringLengthMin;
            _stringLengthMax = stringLengthMax;
        }

        //  Other Methods  --------------------------------
        
        /// <summary>
        /// Performs the validation using the current field type,
        /// field value, and any validation arguments.
        ///
        /// Any thrown <see cref="ContentValidationException"/> will
        /// show helpful text in the inspector to the game maker.
        /// 
        /// </summary>
        /// <param name="args"></param>
        /// <exception cref="ContentValidationException"></exception>
        public override void Validate(ContentValidationArgs args)
        {
            ValidationFieldWrapper validationField = args.ValidationField;
            IContentObject content = args.Content;
            Type type = validationField.FieldType;
            object obj = validationField.GetValue();
            
            if (typeof(Optional).IsAssignableFrom(type))
            {
                Optional optional = obj as Optional;
                if (!optional.HasValue) return;
                type = optional.GetOptionalType();
                obj = optional.GetValue();
            }

            // Validation: Is it a string?
            if (ValidationAttribute.IsNumericType(type))
            {
                throw new ContentValidationException(content, validationField, STRING_TYPE );  
            }

            // Validation: Are the arguments correct?
            if (_stringLengthMin > _stringLengthMax)
            {
                throw new ContentValidationException(content, validationField, 
                    string.Format(ARGUMENT_ERROR, _stringLengthMin, _stringLengthMax)); 
            }

            // Validation: Is the current value correct?
            string stringValue = obj as string;
            if (stringValue == null || 
                !(stringValue.Length >= _stringLengthMin && stringValue.Length <= _stringLengthMax))
            {
                throw new ContentValidationException(content, validationField, 
                    string.Format(VALUE_ERROR, stringValue.Length, _stringLengthMin, _stringLengthMax));
            }
        }
    }
}
```

**Optional Value**

Beamable includes a suite of "optional" datatypes. Here the game maker must set the checkbox to true in the inspector before populating the field. The "optional" functionality and the "validation" functionality may be combined too.

![Optional Value](../../../../../../../media/imgs/optional.png)
