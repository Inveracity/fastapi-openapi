from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.item_response import ItemResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    skip: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 10,
) -> Dict[str, Any]:
    url = "{}/items/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "skip": skip,
        "limit": limit,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, List[ItemResponse]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ItemResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, List[ItemResponse]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    skip: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 10,
) -> Response[Union[HTTPValidationError, List[ItemResponse]]]:
    """Read Item

     - **skip**: how many items to skip
    - **limit**: how many items to show

    Args:
        skip (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[HTTPValidationError, List[ItemResponse]]]
    """

    kwargs = _get_kwargs(
        client=client,
        skip=skip,
        limit=limit,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    skip: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 10,
) -> Optional[Union[HTTPValidationError, List[ItemResponse]]]:
    """Read Item

     - **skip**: how many items to skip
    - **limit**: how many items to show

    Args:
        skip (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[HTTPValidationError, List[ItemResponse]]]
    """

    return sync_detailed(
        client=client,
        skip=skip,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    skip: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 10,
) -> Response[Union[HTTPValidationError, List[ItemResponse]]]:
    """Read Item

     - **skip**: how many items to skip
    - **limit**: how many items to show

    Args:
        skip (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[HTTPValidationError, List[ItemResponse]]]
    """

    kwargs = _get_kwargs(
        client=client,
        skip=skip,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    skip: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 10,
) -> Optional[Union[HTTPValidationError, List[ItemResponse]]]:
    """Read Item

     - **skip**: how many items to skip
    - **limit**: how many items to show

    Args:
        skip (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[HTTPValidationError, List[ItemResponse]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            limit=limit,
        )
    ).parsed
