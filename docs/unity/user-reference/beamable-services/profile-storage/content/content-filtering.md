# Content - Filtering

## Content Filtering

Content can be filtered by tag, type, or id. The Content Manager Window can filter the viewable content. Content can be filtered from the SDK as well. 

### Filter Strings

Content filter strings can be entered into the Content Manager's search box, or into the `GetManifest` function in the SDK. Filter strings follow the same conventions that Unity search strings do. The type of the filter is specified first, followed by a `:` character, and the query for the filter is specified last. 

#### Type Filtering

To filter by content type, use the `t` filter constraint. The following table shows examples of type constraints.

| Filter String      | Description                                                         |
| ------------------ | ------------------------------------------------------------------- |
| `t:currency`       | returns all content elements that are of type "currency"            |
| `t:currency items` | returns all content elements that are of type "currency" or "items" |

#### Tag Filtering

To filter by content tag, use the `tag` filter constraint. The following table shows examples of tag constraints.

| Filter String | Description                                                        |
| ------------- | ------------------------------------------------------------------ |
| `tag:a`       | returns all content elements that have the "a" tag                 |
| `tag:a b`     | returns all content elements that have the "a" tag and the "b" tag |

#### Id Filtering

To filter by content id, use the `id` filter constraint, or use no constraint at all. The `id` filter constraint is the default constraint. The following table shows examples of id constraints.

| Filter String | Description                                                    |
| ------------- | -------------------------------------------------------------- |
| `gems`        | returns all content elements that contain "gems" in their name |
| `id:gems`     | returns all content elements that contain "gems" in their name |

#### Compound Filtering

Multiple filter constraints may be combined if separated by a `,` character. The following table shows examples of compound constraints. 

| Filter String          | Description                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| `t:currency, gems`     | returns all content elements that are of type "currency", and contain "gems" in their name |
| `t:currency, tag:base` | returns all content elements that are of type "currency", and have the "base" tag          |
| `gems, tag:a`          | returns all content elements that contain "gems" in their name, and have the "a" tag       |

### Structured Filtering

In the SDK, the `GetManifest` function accepts a filter string, as shown in the example below.

```csharp
public async Promise<IList<IContentObject>> LoadMyTaggedContent(string tag)
{
    var ctx = BeamContext.Default;

    // load a manifest that only has content including the request tag
    var manifest = await ctx.Content.GetManifest($"tag:{tag}");

    // resolve all the content in that manifest
    var content =  await manifest.ResolveAll();

    return content;
}	
```

Filter strings do not grant type safety in the SDK, and are more prone to bugs and unintentional filtering. The above sample can be re-written with the `ContentQuery` class instead of the filter string. The `ContentQuery` allows the developer to specify constraints in a type safe way and will avoid filter serialization bugs. 

```csharp
public async Promise<IList<IContentObject>> LoadMyTaggedContent(string tag)
{
   var ctx = BeamContext.Default;
   var manifest = await ctx.Content.GetManifest(new ContentQuery
   {
     TagConstraints = new HashSet<string>{ tag }
   });
   var content =  await manifest.ResolveAll();
   return content;
}
```
